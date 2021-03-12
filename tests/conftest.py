from src.domain.User import User
from src import create_app
from src.config.Environment import db,upgrade
import pytest

@pytest.fixture(scope='module')
def newUser():
    user = User('testUserName','testPassword')
    return user

@pytest.fixture(scope='module')
def testClient():
    flaskApp = create_app('test')
    with flaskApp.test_client() as testClient:
        with flaskApp.app_context():
            db.drop_all()
            db.create_all()
            upgrade('./resources/migration/main/')
            yield testClient

        