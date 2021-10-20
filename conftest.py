import pytest

from recipes import create_app
from recipes.extensions import db


@pytest.fixture
def app():
    return create_app("test")


@pytest.fixture
def init_db():
    db.create_all()
    yield
    db.drop_all()
