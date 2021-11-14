import requests


class Spoonacular:

    def __init__(self, app=None, api_url=None, api_key=None):
        self.api_url = api_url
        self.api_key = api_key
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.api_url = app.config["SPOONACULAR_API_URL"]
        self.api_key = app.config["SPOONACULAR_API_KEY"]

    def find_ingredients(self, query):
        res = requests.get(f"{self.api_url}/food/ingredients/autocomplete",
                           params={
                               "number": 10,
                               "query": query,
                               "apiKey": self.api_key
                           })
        data = res.json()
        return data
