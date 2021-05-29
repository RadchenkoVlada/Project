import os
from datetime import date

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

"""the application factory function"""
def create_app():
    from flaskr.models import Car
    from flaskr.models import Contract
    from flaskr.models import User
    from flaskr.models import Brand
    from flaskr.models import Location
    from flaskr.models import CarType

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.DevConfig')
    db.init_app(app)
    migrate.init_app(app, db)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        """
        This function just responds to the browser ULR
        localhost:5000/
        """
        return 'Hello, World!'

    return app
