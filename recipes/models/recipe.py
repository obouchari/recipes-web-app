import datetime
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates

from recipes.extensions import db

recipe_tags = db.Table("recipe_tags",
                       db.Column("recipe_id", UUID(as_uuid=True), db.ForeignKey("recipes.id")),
                       db.Column("tag_id", UUID(as_uuid=True), db.ForeignKey("tags.id")))


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    category = db.Column(db.String, nullable=False, default="main-dish")
    instructions = db.Column(db.Text, nullable=False)
    notes = db.Column(db.Text)
    difficulty = db.Column(db.Enum("Easy", "Medium", "Hard", name="difficulty"), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    serving = db.Column(db.Integer, nullable=False, default=2)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    image = db.Column(db.Text)

    # Recipe owner relationship
    creator_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)
    creator = db.relationship("User", uselist=False, back_populates="recipes")

    # Recipe tags relationship
    tags = db.relationship("Tag",
                           secondary=recipe_tags,
                           backref=db.backref("recipes", lazy="dynamic", cascade="all, delete"),
                           lazy="dynamic")

    # Ratings of a recipe relationship
    ratings = db.relationship("Rating", back_populates="recipe", cascade="all, delete")

    @hybrid_property
    def rating(self) -> float:
        ratings_count = len(self.ratings)
        if ratings_count < 1:
            return ratings_count

        ratings_sum = sum(rating.rating for rating in self.ratings)
        return round(ratings_sum / ratings_count, 1)

    # Ingredient measurement of a recipe relationship
    measurements = db.relationship("Measurement", back_populates="recipe", cascade="all, delete")

    # @validates("name")
    # def validate_name(self, key, name):
    #     if not name or len(name) < 3:
    #         raise ValidationException(message="Name is invalid")
    #     return name

    def __repr__(self):
        return 'RecipeModel(' \
               'name=%s, ' \
               'description=%s, ' \
               'instructions=%s, ' \
               'notes=%s, ' \
               'difficulty=%s, ' \
               'image=%s)' % (
                   self.name,
                   self.description,
                   self.instructions,
                   self.notes,
                   self.difficulty,
                   self.image)

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find(cls, recipe_id):
        return cls.query.get_or_404(recipe_id)

    @classmethod
    def find_by_name(cls, recipe_name):
        return cls.query.filter_by(name=recipe_name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
