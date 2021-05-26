from flaskr import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)

    # TODO: handle passwords in a secure way
    password = db.Column(db.String(15), unique=True, nullable=False)

    contracts = db.relationship('Contract', backref='user', lazy=True)

    def __repr__(self):
        return f"<User id={self.id} first_name={self.first_name} last_name={self.last_name}>"
