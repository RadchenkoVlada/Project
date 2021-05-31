from flaskr import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(200), unique=True, nullable=False)

    hashed_password = db.Column(db.String(200), unique=False, nullable=False)

    # this foreign key is implemented as "One To Many" from https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
    # because user.contracts will be useful in the code unlike brand.cars which is implemented as "Many To One"
    contracts = db.relationship('Contract', backref='user', lazy=True)

    def set_password(self, password):
        """Create hashed password."""
        self.hashed_password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.hashed_password, password)


    def __repr__(self):
        return f"<User id={self.id} first_name={self.first_name} last_name={self.last_name}>"
