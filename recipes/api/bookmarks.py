from flask import request
from flask_jwt_extended import jwt_required, current_user
from flask_restx import Resource

from recipes.extensions import api
from recipes.models import Recipe
from recipes.schemas import BookmarkSchema, RecipeSchema
from recipes.shared.error_handler import error_handler


@api.route("/bookmarks", endpoint="bookmarks")
class BookmarkEndpoint(Resource):

    @jwt_required()
    @error_handler()
    def get(self):
        """Get a list of bookmarked recipes of the current user (logged in user)"""
        recipe_schema = RecipeSchema(many=True, exclude=("tags", "creator", "measurements"))
        bookmarks = current_user.bookmarked_recipes.all()

        return {
            "total": len(bookmarks),
            "data": recipe_schema.dump(bookmarks)
        }

    @jwt_required()
    @error_handler()
    def post(self):
        """Bookmark a recipe"""
        request_bookmark_schema = BookmarkSchema()
        recipe_id = request_bookmark_schema.load(data=request.json).get("recipe_id")
        recipe = Recipe.find(recipe_id=recipe_id)

        if recipe in current_user.bookmarked_recipes.all():
            current_user.bookmarked_recipes.remove(recipe)
        else:
            current_user.bookmarked_recipes.append(recipe)

        current_user.save()

        return {
                   "message": "success"
               }, 201
