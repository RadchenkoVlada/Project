import decimal

from flask_restful import reqparse, abort, Resource, fields, marshal_with
from flaskr.models import Car
from flaskr.models import Brand
from flaskr.models import Location
from flaskr.models import CarType
from flaskr import db


class CarAPI(Resource):
    @staticmethod
    def to_dict(car):
        return {'name': car.name, 'car_type': car.car_type.name, 'brand': car.brand.name, 'location': car.location.name,
                      'price_per_day': float(car.price_per_day), 'air_conditioning': car.air_conditioning}

    def get(self, car_id):
        car = Car.query.get(car_id)
        if car is None:
            abort(404, message=f"Car {car_id} doesn't exist")

        return CarAPI.to_dict(car)


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('car_type', type=str)
        parser.add_argument('brand', type=str)
        parser.add_argument('location', type=str)
        parser.add_argument('price_per_day', type=float)
        parser.add_argument('air_conditioning', type=bool)

        args = parser.parse_args()

        car_type = CarType.query.filter_by(name=args['car_type']).one_or_none()
        brand = Brand.query.filter_by(name=args['brand']).one_or_none()
        location = Location.query.filter_by(name=args['location']).one_or_none()

        error_message = ""
        if car_type is None:
            error_message += f"car_type {args['car_type']} doesn't exists. "
        if brand is None:
            error_message += f"brand {args['brand']} doesn't exists. "
        if location is None:
            error_message += f"location {args['location']} doesn't exists."

        if error_message:
            abort(404, message=error_message)

        new_car = Car(name=args[ 'name' ], price_per_day=decimal.Decimal(args[ 'price_per_day' ]),
            air_conditioning=args[ 'air_conditioning' ],
            brand=brand, car_type=car_type, location=location)

        db.session.add(new_car)
        db.session.commit()

        return CarAPI.to_dict(new_car), 201


    def delete(self, car_id):
        car = Car.query.filter_by(id=car_id)

        # if car.exist() is None:
        #     abort(404, message=f"Car {car_id} doesn't exist")
        deleted_count = car.delete()
        db.session.commit()

        if deleted_count:
            return '', 200
        else:
            abort(404, message=f"Car {car_id} doesn't exist")
