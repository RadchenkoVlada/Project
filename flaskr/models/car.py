from flaskr import db


class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    photo_filename = db.Column(db.String(20))

    ref_car_type = db.Column(db.Integer, db.ForeignKey('car_types.id'), nullable=False)
    car_type = db.relationship("CarType")

    ref_brand = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    brand = db.relationship("Brand")

    ref_location = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    location = db.relationship("Location")

    num_of_passangers = db.Column(db.Integer)
    price_per_day = db.Column(db.Numeric)
    air_conditioning = db.Column(db.Boolean)
    automatic_transmission = db.Column(db.Boolean)
    doors_4 = db.Column(db.Boolean)

    contracts = db.relationship('Contract', backref='car', lazy=True)

    def __repr__(self):
        return f"<Car id={self.id}, name={self.name}>"

    def get_photo_path(self):
        return "/static/img/cars/" + self.photo_filename
