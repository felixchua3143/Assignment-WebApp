from wtforms import (Form, StringField, RadioField, SelectField, TextAreaField, validators, IntegerField,
                     SelectMultipleField)
from wtforms.fields import EmailField, DateField


class CreateUserForm(Form):
    user_type = RadioField('Rider/Driver?', choices=[('R', 'Rider'), ('D', 'Driver')])
    name = StringField('Name',[validators.Length(min=1, max=150), validators.DataRequired()])
