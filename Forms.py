from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, DecimalField, DecimalRangeField, validators

class CreateCarbonForm(Form):
    electricity =  DecimalField("Electricity", [validators.input_required(message= "Please eneter a number")])
    if electricity.isalpha():
        state = True
    else:
        state = False
