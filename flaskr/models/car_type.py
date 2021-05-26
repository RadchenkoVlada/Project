from flaskr import db


class CarType(db.Model):
    __tablename__ = 'car_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"<CarType id={self.id}, name={self.name}>"
