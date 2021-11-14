import uuid
from sqlalchemy.dialects.postgresql import UUID

from recipes.extensions import db


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(60), nullable=False, unique=True)

    # Recipe category relationship
    recipes = db.relationship("Recipe", back_populates="category")

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find(cls, category_id):
        return cls.query.get_or_404(category_id)

    @classmethod
    def find_by_name(cls, category_name):
        return cls.query.filter_by(name=category_name).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
