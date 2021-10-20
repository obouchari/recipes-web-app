from recipes.extensions import db


class Recipe(db.Model):
    __tablename__ = "recipes"
