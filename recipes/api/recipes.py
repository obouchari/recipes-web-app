from flask import request
from flask_jwt_extended import jwt_required, current_user
from flask_restx import Resource
from marshmallow import ValidationError

from recipes.extensions import api
from recipes.models import Recipe
from recipes.schemas import RecipeSchema
from recipes.shared.error_handler import error_handler
from recipes.shared.error_types import CONFLICT_EXCEPTION


@api.route("/recipes", endpoint="recipes_list")
class RecipeListEndpoint(Resource):

    @error_handler()
    def get(self):
        recipe_schema = RecipeSchema(many=True)
        recipes = Recipe.all()

        return {
            "total": len(recipes),
            "data": recipe_schema.dump(recipes)
        }

    @jwt_required()
    @error_handler()
    def post(self):
        recipe_name = request.json.get("name")
        recipe_exists = Recipe.find_by_name(recipe_name=recipe_name)
        if recipe_exists:
            raise ValidationError({"message": f"A recipe with the name {recipe_name} already exists.",
                                   **CONFLICT_EXCEPTION})

        request_recipe_schema = RecipeSchema()
        recipe = request_recipe_schema.load(data=request.json)
        recipe.creator = current_user
        recipe.save()
        return {
                   "message": "Success",
                   "_links": [
                       {
                           "rel": "self",
                           "href": f"{request.base_url}/{recipe.id}",
                           "action": "GET"
                       }
                   ]
               }, 201


@api.route("/recipes/<uuid:recipe_id>", endpoint="recipe")
class RecipeEndpoint(Resource):

    @error_handler()
    def get(self, recipe_id):
        recipe_schema = RecipeSchema()
        recipe = Recipe.find(recipe_id=recipe_id)

        return {
            "data": recipe_schema.dump(recipe)
        }

    @jwt_required()
    @error_handler()
    def put(self, recipe_id):
        pass

    @jwt_required()
    @error_handler()
    def patch(self, recipe_id):
        pass

    @jwt_required()
    @error_handler()
    def delete(self, recipe_id):
        recipe = Recipe.find(recipe_id=recipe_id)
        recipe.delete()
        return {
            "message": "success"
        }
