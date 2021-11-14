import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    # SOME_API_KEY = os.getenv("SOME_API_KEY", "default key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    SPOONACULAR_API_URL = "https://api.spoonacular.com"
    SPOONACULAR_API_KEY = os.getenv("SPOONACULAR_API_KEY")


class DevConfig(BaseConfig):
    EXPLAIN_TEMPLATE_LOADING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # JSON_SORT_KEYS = False
    JWT_COOKIE_SECURE = False


class ProdConfig(BaseConfig):
    JWT_COOKIE_SECURE = True


class TestConfig(BaseConfig):
    TESTING = True


configurations = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "test": TestConfig
}
