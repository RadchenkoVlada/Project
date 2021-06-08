from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    """User Registration Form."""
    first_name = StringField(
        'First name',
        validators=[
            DataRequired(),
            Length(max=80)
        ]
    )
    last_name = StringField(
        'Last name',
        validators=[
            DataRequired(),
            Length(max=80)
        ]
    )
    phone_number = StringField(
        'Phone',
        validators=[
            DataRequired(),
            Length(max=15)
        ]
    )
    email = StringField(
        'Your email address',
        validators=[
            DataRequired(),
            Length(max=120),
            Email(message='Enter a valid email.')
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8, message='PASSWORD_INVALID_LENGTH')
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField('Create an Account')
