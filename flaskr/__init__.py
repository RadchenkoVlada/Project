import os
from datetime import date

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

"""the application factory function"""
def create_app(test_config=None):
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

    # a simple pages to test models
    # this is a test code just to make sure db works, sb creattion should be reworked to migrations
    @app.route('/test')
    def test():
        from flaskr.models import Car
        from flaskr.models import Contract
        from flaskr.models import User
        from flaskr.models import Brand
        from flaskr.models import Location
        from flaskr.models import CarType

        db.create_all()

        l1 = Location(id=1, name='Kharkiv')
        l2 = Location(id=2, name='Kiev')
        l3 = Location(id=3, name='Odessa')
        b1 = Brand(id=1, name='BMW')
        b2 = Brand(id=2, name='Toyota')
        c = CarType(id=1, name='type1')
        c2 = CarType(id=2, name='type2')
        car = Car(id=1, name='first_car', car_type=c, brand=b1, location=l2, num_of_passangers=3, price_per_day=10,
                  air_conditioning=True, automatic_transmission=True, doors_4=False)
        db.session.add(l1)
        db.session.add(l2)
        db.session.add(l3)
        db.session.add(b1)
        db.session.add(b2)
        db.session.add(c)
        db.session.add(c2)
        db.session.add(car)

        u1 = User(id=1, first_name='Andrew', last_name='Smith', email='test@gmail.com', phone_number="0123456789", password='test_pass')
        u2 = User(id=2, first_name='Tom', last_name='Smith', email='test2@gmail.com', phone_number="9876543210", password='test_pass2')

        first_car = Car.query.all()[0]

        con1 = Contract(id=1, pick_up_date=date(2021, 4, 16), drop_off_date=date.today(), total_price=400, car=first_car, user=u1)
        con2 = Contract(id=2, pick_up_date=date(2008, 6, 24), drop_off_date=date.today(), total_price=47190, car=first_car, user=u2)

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(con1)
        db.session.add(con2)

        db.session.commit()

        #
        # l1 = User(id=1, name='Kharkiv')
        # l2 = Location(id=1, name='Kiev')
        # l3 = Location(id=1, name='Odessa')
        # b1 = Brand(id=1, name='BMW')
        # b2 = Brand(id=2, name='Toyota')
        # l2
        # l2.id = 2
        # l3.id = 3
        # c = CarType(id=1, name='type1')
        # c2 = CarType(id=2, name='type2')
        # car = Car(id=1, name='first_car', car_type=c, brand=b1, location=l2, num_of_passangers=3, price_per_day=10,
        #           air_conditioning=True, automatic_transmission=True, doors_4=False)
        # db.session.add(l1)
        # db.session.add(l2)
        # db.session.add(l3)
        # db.session.add(b1)
        # db.session.add(b2)
        # db.session.add(c)
        # db.session.add(c2)
        # db.session.add(car)
        # db.session.commit()

        from flaskr.models import Car
        return 'Done'

    return app
