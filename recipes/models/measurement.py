from sqlalchemy.dialects.postgresql import UUID

from recipes.extensions import db


class Measurement(db.Model):
    __tablename__ = "measurement_details"

    recipe_id = db.Column(UUID(as_uuid=True), db.ForeignKey("recipes.id"), primary_key=True)
    ingredient_id = db.Column(UUID(as_uuid=True), db.ForeignKey("ingredients.id"), primary_key=True)
    details = db.Column(db.String(255), nullable=False)

    recipe = db.relationship("Recipe", back_populates="measurements")
    ingredient = db.relationship("Ingredient")
