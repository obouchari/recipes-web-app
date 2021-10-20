import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    SOME_API_KEY = os.getenv("SOME_API_KEY", "default key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class DevConfig(BaseConfig):
    EXPLAIN_TEMPLATE_LOADING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class ProdConfig(BaseConfig):
    pass


class TestConfig(BaseConfig):
    TESTING = True


configurations = {
    "dev": DevConfig,
    "prod": ProdConfig,
    "test": TestConfig
}
