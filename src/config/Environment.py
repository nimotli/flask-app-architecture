from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,upgrade

db = SQLAlchemy()
migrate = Migrate()
