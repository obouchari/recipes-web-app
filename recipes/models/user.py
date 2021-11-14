import uuid
import datetime

from marshmallow import ValidationError
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import validates
from email_validator import validate_email, EmailNotValidError

from recipes.extensions import db, bcrypt
from recipes.shared.error_types import VALIDATION_EXCEPTION, AUTHENTICATION_EXCEPTION, CONFLICT_EXCEPTION

bookmarks = db.Table("bookmarks",
                     db.Column("user_id", UUID(as_uuid=True), db.ForeignKey("users.id")),
                     db.Column("recipe_id", UUID(as_uuid=True), db.ForeignKey("recipes.id")))

followers = db.Table("followers",
                     db.Column("follower_id", UUID(as_uuid=True), db.ForeignKey("users.id")),
                     db.Column("following_id", UUID(as_uuid=True), db.ForeignKey("users.id")))


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    profile_photo = db.Column(db.Text)

    # Recipe owner relationship
    recipes = db.relationship("Recipe", back_populates="creator", cascade="all,delete")

    # Bookmark a recipe relationship
    bookmarked_recipes = db.relationship("Recipe",
                                         secondary=bookmarks,
                                         backref=db.backref("users", lazy="dynamic", cascade="all, delete"),
                                         lazy="dynamic")

    ratings = db.relationship("Rating", back_populates="rater")

    following = db.relationship("User",
                                secondary=followers,
                                primaryjoin=(followers.c.follower_id == id),
                                secondaryjoin=(followers.c.following_id == id),
                                backref=db.backref("followers", lazy="dynamic"),
                                lazy="dynamic")

    @validates("email")
    def validate_email(self, key, email):
        try:
            valid = validate_email(email)
            email = valid.email
            return email
        except EmailNotValidError:
            raise ValidationError({
                "message": "Email address is invalid",
                **VALIDATION_EXCEPTION
            })

    @classmethod
    def find_by_email(cls, email: str):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def register(cls, first_name: str, last_name: str, email: str, password: str):
        """Save a user if not already present in database"""
        existing_user = cls.find_by_email(email=email)

        if existing_user:
            raise ValidationError({
                "message": "Email address is already taken",
                **CONFLICT_EXCEPTION
            })

        hashed = bcrypt.generate_password_hash(password=password)
        hashed_utf8 = hashed.decode("utf8")
        user = cls(first_name=first_name, last_name=last_name, email=email, password=hashed_utf8)
        user.save()
        return user

    @classmethod
    def authenticate(cls, email, password):
        user = cls.find_by_email(email=email)
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        raise ValidationError({
            "message": "invalid email or password",
            **AUTHENTICATION_EXCEPTION
        })

    def follow(self, user):
        if not self.is_following(user):
            self.following.append(user)
            db.session.commit()

    def unfollow(self, user):
        if self.is_following(user):
            self.following.remove(user)
            db.session.commit()

    def is_following(self, user):
        return self.following.filter(followers.c.following_id == user.id).count() > 0

    def bookmark(self, recipe):
        if not self.is_bookmarked(recipe):
            self.bookmarked_recipes.append(recipe)
            db.session.commit()

    def unbookmark(self, recipe):
        if self.is_bookmarked(recipe):
            self.bookmarked_recipes.remove(recipe)
            db.session.commit()

    def is_bookmarked(self, recipe):
        return self.bookmarked_recipes.filter(bookmarks.recipe_id == recipe.id).count() > 0

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def find(cls, user_id):
        return cls.query.filter_by(id=user_id).one_or_none()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
