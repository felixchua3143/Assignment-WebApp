from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators

class CreateUserForm(Form):
    electricity = StringField('electricity', [validators.Length(min=1, max=150), validators.DataRequired()])
    num_household = StringField('num_household', [validators.Length(min=1, max=150), validators.DataRequired()])
    # gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    # membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    # remarks = TextAreaField('Remarks', [validators.Optional()])


    water = StringField('water', [validators.Length(min=1, max=150), validators.DataRequired()])
    gas = StringField('gas', [validators.Length(min=1, max=150), validators.DataRequired()])
    food = StringField('food', [validators.Length(min=1, max=150), validators.DataRequired()])