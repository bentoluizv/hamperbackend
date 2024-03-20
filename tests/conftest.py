import os

import pytest

from project import create_app_wsgi
from project.ext.database import db


@pytest.fixture
def app_testing():
    os.environ['FLASK_ENV'] = 'testing'
    app = create_app_wsgi()
    with app.app_context():
        db.create_all()


    yield app

    with app.app_context():
        db.drop_all()