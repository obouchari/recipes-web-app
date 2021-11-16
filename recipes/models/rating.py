import datetime

from sqlalchemy.dialects.postgresql import UUID

from recipes.extensions import db


class Rating(db.Model):
    __tablename__ = "ratings"

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), primary_key=True)
    recipe_id = db.Column(UUID(as_uuid=True), db.ForeignKey("recipes.id"), primary_key=True)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String(20000))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    recipe = db.relationship("Recipe", back_populates="ratings")
    rater = db.relationship("User", back_populates="ratings")

    @classmethod
    def find(cls, user_id, recipe_id):
        return cls.query.filter_by(user_id=user_id, recipe_id=recipe_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
