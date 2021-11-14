from flask import request
from flask_jwt_extended import jwt_required, current_user
from flask_restx import Resource

from recipes.extensions import api
from recipes.models import Rating, Recipe
from recipes.schemas import RatingSchema
from recipes.shared.error_handler import error_handler


@api.route("/ratings", endpoint="ratings")
class RatingEndpoint(Resource):

    @jwt_required()
    @error_handler()
    def post(self):
        """Rate a recipe"""
        request_rating_schema = RatingSchema()
        rating_payload = request_rating_schema.load(data=request.json)
        recipe_id = rating_payload.get("recipe_id")

        rating = Rating.find(user_id=current_user.id, recipe_id=recipe_id)

        if rating:
            rating.rating = rating_payload.get("rating")
        else:
            recipe = Recipe.find(recipe_id=recipe_id)
            rating = Rating(
                rating=rating_payload.get("rating"),
                recipe=recipe,
                rater=current_user
            )

        rating.save()

        return {
                   "message": "success"
               }, 201
