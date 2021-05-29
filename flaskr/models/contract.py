from flaskr import db


class Contract(db.Model):
    __tablename__ = 'contracts'

    id = db.Column(db.Integer, primary_key=True)

    pick_up_date = db.Column(db.DateTime, nullable=False)
    drop_off_date = db.Column(db.DateTime, nullable=False)

    total_price = db.Column(db.Numeric, nullable=False)
    ref_car = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable=False)
    ref_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"<Contract id={self.id}, ref_car={self.ref_car}, ref_user={self.ref_user}>"
