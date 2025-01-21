from wtforms import Form, StringField, IntegerField, SelectField, SelectMultipleField, validators


class CarbonCalForm(Form):
    electricity = SelectField("Electricity Usage", choices=[("e < $50", "< $50"), ("e $50 - $100","$50 - $100"), ("e $101 - $150", "$101 - $150"), ("e $151 - $200", "$151 - $200"), ("e > $200", "> $200")])
    gas = SelectField("Gas", choices=[("g $0", "$0"), ("g < $10", "< $10"), ("g $11 - $15", "$11 - $15"), ("g $16 - $20", "$16 - $20"), ("g > $20", "> $20")])
    water = SelectField("Water", choices=[("w < $25", "< $25"), ("w $25 - $50", "$25 - $50"), ("w $51 - $70", "$51 - $70"), ("w $71 - $90", "$71 - $90"), ("w > $90", "> $90")])
    num_household = IntegerField("Number of People In Household")
    food = SelectMultipleField("Food (ctrl+click to select multiple options", choices=[("beef", "Beef"), ("eggs", "Eggs"), ("pork", "Pork"), ("vegetables", "Vegetables"), ("chicken_duck", "Chicken and Duck"), ("fruits", "Fruits"), ("mutton", "Mutton"), ("grains","Grains"), ("seafood", "Seafood"), ("dairy_prod", "Dairy Products")])

