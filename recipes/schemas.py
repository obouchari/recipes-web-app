from marshmallow import fields, pre_load, ValidationError

from recipes.extensions import ma, db
from recipes.models import Recipe, Category, Ingredient, Measurement, Tag, User
from recipes.shared.error_types import NOT_FOUND_EXCEPTION


class RecipeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Recipe
        load_instance = True
        sqla_session = db.session

    creator = ma.Nested("UserSchema", only=("id", "first_name", "last_name", "profile_photo"))
    category = ma.Nested("CategorySchema", only=("id", "name"))
    tags = ma.Nested("TagSchema", many=True, exclude=("recipes",))
    measurements = ma.Nested("MeasurementSchema", many=True)
    rating = fields.Float()


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True
        sqla_session = db.session

    recipes = ma.Nested("RecipeSchema", many=True, exclude=("category",))


class IngredientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ingredient
        load_instance = True
        sqla_session = db.session


class MeasurementSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Measurement
        load_instance = True
        sqla_session = db.session

    ingredient = ma.Nested("IngredientSchema")


class TagSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tag
        load_instance = True
        sqla_session = db.session

    recipes = ma.Nested("RecipeSchema", many=True, exclude=("tags",))


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session


class BookmarkSchema(ma.Schema):
    recipe_id = fields.Str(required=True, load_only=True)

    @pre_load
    def check_recipe_exists(self, in_data, **kwargs):
        recipe = Recipe.find(recipe_id=in_data["recipe_id"])
        if not recipe:
            raise ValidationError({"message": f"A recipe with the id {in_data['recipe_id']} doesn't exist.",
                                   **NOT_FOUND_EXCEPTION})
        return in_data


class RatingSchema(ma.Schema):
    recipe_id = fields.Str(required=True, load_only=True)
    rating = fields.Float(required=True, load_only=True)

    @pre_load
    def check_recipe_exists(self, in_data, **kwargs):
        recipe = Recipe.find(recipe_id=in_data["recipe_id"])
        if not recipe:
            raise ValidationError({"message": f"A recipe with the id {in_data['recipe_id']} doesn't exist.",
                                   **NOT_FOUND_EXCEPTION})
        return in_data
