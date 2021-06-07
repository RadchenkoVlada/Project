from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.fields.html5 import DateTimeLocalField
from wtforms.validators import DataRequired, Email, Length


class SearchForm(FlaskForm):
    """User Log-in Form."""
    location = SelectField('Location')

    # pick_up_date = DateTimeLocalField("Pick-up date", format="%d.%m.%Y, %H:%M")
    # pick_up_date = DateTimeLocalField("Pick-up date", format="%Y.%m.%dT%H:%M")
    pick_up_date = DateTimeLocalField("Pick-up date", format="%Y-%m-%dT%H:%M")
    # pick_up_date = DateTimeLocalField("Pick-up date", format="yyyy-mm-ddThh:mm")
    # drop_off_date = DateTimeLocalField("Drop-off date", format="yyyy-mm-ddThh:mm")
    drop_off_date = DateTimeLocalField("Drop-off date", format="%Y-%m-%dT%H:%M")
    # drop_off_date = DateTimeLocalField("Drop-off date", format="%Y.%m.%dT%H:%Mx")
    # drop_off_date = DateTimeLocalField("Drop-off date", format="%d.%m.%Y, %H:%M")
    submit = SubmitField('Search')
