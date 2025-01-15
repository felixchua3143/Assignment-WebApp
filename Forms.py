from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators, DateField, DecimalField, SubmitField


class CreateGraphForm(Form):
    date = DateField("Date", validators=None, format="%Y-%m-%d")
    value = DecimalField("Value", places=2)
    submit = SubmitField("Submit Value")