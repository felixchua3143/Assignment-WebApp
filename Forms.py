from wtforms import Form, StringField, IntegerField, SelectField, SelectMultipleField, validators

class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])

class CarbonCalForm(Form):
    electricity = SelectField("Electricity Usage ($)", [validators.InputRequired])
    gas = SelectField("Gas ($)", validators.InputRequired)
    water = SelectField("Water ($)", validators.InputRequired)
    num_household = IntegerField("Number of People In Household", validators.InputRequired)