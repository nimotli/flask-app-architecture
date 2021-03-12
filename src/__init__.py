
from flask import Flask
from src.config.Blueprint import registerBluePrints
from flask_jwt import JWT, jwt_required, current_identity
from src.config.DatabaseConfiguration import init_db
from src.config.Environment import db,migrate
from src.config.AuthenticationProvider import authenticate,identity
from src.config.Configure import configure_app
import os

def create_app(profile="dev"):
    app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    app,env = configure_app(app,profile)
    jwt = JWT(app, authenticate, identity)
    app = init_db(app,env)
    db.init_app(app)
    '''
    Add any created model that you want to be added to the migration-able models list
    '''
    from  src.domain import User
    migrate.init_app(app, db)
    app = registerBluePrints(app)
    return app