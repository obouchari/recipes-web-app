from flask_restx import Resource

from recipes.extensions import api, spoonacular
from recipes.models import Ingredient
from recipes.shared.error_handler import error_handler


@api.route("/ingredients/autocomplete/<string:query>", endpoint="ingredients_autocomplete")
class IngredientsAutoCompleteEndpoint(Resource):

    @error_handler()
    def get(self, query):
        ingredients = spoonacular.find_ingredients(query)
        return {
            "ingredients": ingredients
        }
