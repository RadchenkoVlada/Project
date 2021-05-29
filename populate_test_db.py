import flaskr
from datetime import date
from flaskr.models import *


def delete_all_data_from_db(db):
    # The order is important because of foreign keys.
    # We should delete the tables without foreign keys(references) to them first.
    Contract.query.delete()
    User.query.delete()
    Car.query.delete()
    Brand.query.delete()
    Location.query.delete()
    CarType.query.delete()

    db.session.commit()


def create_simple_small_test_db(db):
    l1 = Location(id=1, name='Kharkiv')
    l2 = Location(id=2, name='Kiev')
    l3 = Location(id=3, name='Odessa')
    b1 = Brand(id=1, name='BMW')
    b2 = Brand(id=2, name='Toyota')
    c1 = CarType(id=1, name='type1')
    c2 = CarType(id=2, name='type2')
    car = Car(id=1, name='first_car', car_type=c1, brand=b1, location=l2, num_of_passangers=3, price_per_day=10,
              air_conditioning=True, automatic_transmission=True, doors_4=False)

    u1 = User(id=1, first_name='Andrew', last_name='Smith', email='test@gmail.com', phone_number="0123456789",
              password='test_pass')
    u2 = User(id=2, first_name='Tom', last_name='Smith', email='test2@gmail.com', phone_number="9876543210",
              password='test_pass2')

    con1 = Contract(id=1, pick_up_date=date(2021, 4, 16), drop_off_date=date.today(), total_price=400, car=car,
                    user=u1)
    con2 = Contract(id=2, pick_up_date=date(2008, 6, 24), drop_off_date=date.today(), total_price=47190, car=car,
                    user=u2)

    db.session.add_all((l1, l2, l3))
    db.session.add_all((b1, b2))
    db.session.add_all((c1, c2))
    db.session.add(car)
    db.session.add_all((u1, u2))
    db.session.add_all((con1, con2))

    db.session.commit()


# A simple script in order to easily populate test data
if __name__ == '__main__':
    app = flaskr.create_app()
    app.app_context().push()

    delete_all_data_from_db(flaskr.db)
    create_simple_small_test_db(flaskr.db)
    print('Done')
