from wtforms import Form, IntegerField, SelectField, SelectMultipleField, validators
from wtforms.validators import ValidationError


def sel_one_valid(form, field):
    if field.data == "sel_o":
        raise ValidationError("Please pick an option")
    else:
        pass

class CarbonCalForm(Form):
    electricity = SelectField("Electricity", [validators.DataRequired(), sel_one_valid],
                              choices=[("sel_o", "Select One"), ("e < $50", "< $50"),
                                       ("e $50 - $100", "$50 - $100"),
                                       ("e $101 - $150", "$101 - $150"),
                                       ("e $151 - $200", "$151 - $200"), ("e > $200", "> $200")])
    gas = SelectField("Gas", [validators.DataRequired(), sel_one_valid],
                      choices=[("sel_o", "Select One"), ("g $0", "$0"), ("g < $10", "< $10"),
                               ("g $11 - $15", "$11 - $15"),
                               ("g $16 - $20", "$16 - $20"), ("g > $20", "> $20")])
    water = SelectField("Water", [validators.DataRequired(), sel_one_valid],
                        choices=[("sel_o", "Select One"), ("w < $25", "< $25"), ("w $25 - $50", "$25 - $50"),
                                 ("w $51 - $70", "$51 - $70"),
                                 ("w $71 - $90", "$71 - $90"), ("w > $90", "> $90")])
    num_household = IntegerField("Number of People In Household", [validators.DataRequired(), sel_one_valid])
    food = SelectMultipleField("Food (ctrl+click to select multiple options)",
                               [validators.DataRequired(), sel_one_valid],
                               choices=[("sel_o", "Select One"), ("beef", "Beef"), ("eggs", "Eggs"),
                                        ("pork", "Pork"),
                                        ("vegetables", "Vegetables"), ("chicken_duck", "Chicken and Duck"),
                                        ("fruits", "Fruits"), ("mutton", "Mutton"), ("grains", "Grains"),
                                        ("seafood", "Seafood"), ("dairy_prod", "Dairy Products")])
    cloth_foot = SelectField("Clothing and Footwear", [validators.DataRequired(), sel_one_valid],
                             choices=[("sel_o", "Select One"), ("cf $0", "$0"), ("cf < $30", "< $30"),
                                      ("cf $30 - $100", "$30 - $100"),
                                      ("cf > $100", "> $100")])
    recreate_act = SelectField(
        "Recreational and Cultural Activities (Media subscriptions, gym memberships, movie and concert tickets)",
        [validators.DataRequired(), sel_one_valid],
        choices=[("sel_o", "Select One"), ("ra $0", "$0"), ("ra < $30", "< $30"), ("ra $30 - $100", "$30 - $100"),
                 ("ra > $100", "> $100")])
    furn_house_ep_m = SelectField(
        "Furnishings, household equipment, household maintenance (Furniture, home appliances, maintenance, and repairs)",
        [validators.DataRequired(), sel_one_valid],
        choices=[("sel_o", "Select One"), ("f_h $0", "$0"), ("f_h < $100", "< $100"),
                 ("f_h $100 - $300", "$100 - $300"),
                 ("f_h > $300", "> $300")])
    health = SelectField("Health (incl. pharmaceuticals) (Medication, medical appointments (including for pets))",
                         [validators.DataRequired(), sel_one_valid],
                         choices=[("sel_o", "Select One"), ("h $0", "$0"), ("h < $50", "< $50"),
                                  ("h $50 - $200", "$50 - $200"),
                                  ("h > $200", "> $200")])
    com_service = SelectField("Communication services (Mobile phone, internet services, and postage)",
                              [validators.DataRequired(), sel_one_valid],
                              choices=[("sel_o", "Select One"), ("cs $0", "$0"), ("cs < $40", "< $50"),
                                       ("cs $40 - $200", "$40 - $200"),
                                       ("cs > $200", "> $200")])
    edu_service = SelectField("Educational services",[validators.DataRequired(), sel_one_valid],
                              choices=[("sel_o", "Select One"), ("edus $0", "$0"), ("edus < $100", "< $100"),
                                       ("edus $100 - $200", "$100 - $200"),
                                       ("edus > $200", "> $200")])
    others = SelectField("Other purchased goods and services",[validators.DataRequired(), sel_one_valid],
                         choices=[("sel_o", "Select One"), ("o $0", "$0"), ("o < $120", "< $120"),
                                  ("o $120 - $500", "$120 - $500"),
                                  ("o > $500", "> $500")])

class Feedback:
    def __init__(self, name, email, feedback):
        self.name = name
        self.email = email
        self.feedback = feedback

    def to_dict(self):
        return {"name": self.name, "email": self.email, "feedback": self.feedback}
class Review:
    def __init__(self, name, email, product_name, review, rating):
        self.name = name
        self.email = email
        self.product_name = product_name
        self.review = review
        self.rating = rating

    def to_dict(self):
        return {"name": self.name, "email": self.email, "product_name": self.product_name, "review": self.review, "rating": self.rating}


class Support:
    def __init__(self, name, email, issue):
        self.name = name
        self.email = email
        self.issue = issue

    def to_dict(self):
        return {"name": self.name, "email": self.email, "issue": self.issue}
