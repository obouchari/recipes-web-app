from recipes.extensions import db


class User(db.Model):
    __tablename__ = "users"
