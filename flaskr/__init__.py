import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

"""the application factory function"""
def create_app():
    from flaskr.models import Car
    from flaskr.models import Contract
    from flaskr.models import User
    from flaskr.models import Brand
    from flaskr.models import Location
    from flaskr.models import CarType
    from flaskr.service import CarAPI

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.DevConfig')
    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api.add_resource(CarAPI, '/api/cars/', '/api/cars/<car_id>')

    with app.app_context():
        from flaskr import views

    return app
