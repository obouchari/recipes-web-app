import uuid
from sqlalchemy.dialects.postgresql import UUID

from recipes.extensions import db


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(60), nullable=False, unique=True)

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find(cls, ingredient_id):
        return cls.query.get_or_404(ingredient_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
