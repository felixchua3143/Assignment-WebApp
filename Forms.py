from wtforms import *


class CreateGraphForm(Form):
    date = DateField("Date", [validators.input_required], format="%Y-%m-%d")
    value = DecimalField("Value", places=2)
    submit = SubmitField("Submit Value")


class CreateCarbonForm(Form):
    num_household = IntegerField("Number of People in Household:", [validators.input_required])
    electricity = SelectField("Electricity:", [validators.input_required],
                              choices=[("e <50", "<$50"), ("e 50 - 100", "$50 - $100"), ("e 101 - 150", "$101 - $150"),
                                       ("e 151 - 200", "$151 - $200"), ("e >200", ">$200")])
    gas = SelectField("Gas:", [validators.input_required],
                      choices=[("g 0", "$0"), ("g <10", "<$10"), ("g 11 - 15", "$11 - $15"), ("g 16 - 20", "$16 - $20"),
                               ("g >20", ">$20")])
    water = SelectField("Water:", [validators.input_required],
                        choices=[("w <25", "<$25"), ("w 25 - 50", "$25 - $50"), ("w 51 - 70", "$51 - $70"),
                                 ("w 71 - 90", "$71 - $90"),
                                 ("w >90", ">$90")])
    food = SelectMultipleField("Which foods make up part of your diet?", [validators.input_required],
                               choices=[("eggs", "Eggs"), ("vegetables", "Vegetables"), ("fruits", "Fruits"),
                                        ("grains", "Grains"), ("dairy_products", "Dairy Products"), ("beef", "Beef"),
                                        ("pork", "Pork"), ("chicken_duck", "Chicken and Duck"), ("mutton", "Mutton"),
                                        ("seafood", "Seafood")])
    cloth_footwear = SelectField("Clothing and Footwear:", [validators.input_required],
                                 choices=[("cf <30", "<$30"), ("ecf 30 - 100", "$30 - $100"), ("cf >100", ">$100")])
    recreate_act = SelectField("Recreational Activities:", [validators.input_required],
                               choices=[("ra <60", "<$60"), ("ra 60 - 300", "$60 - $300"), ("ra >300", ">$300")])
    furn_house_equipment_maintenance = SelectField("Furnishings, Household Equipment, Household Maintenance:",
                                                   [validators.input_required],
                                                   choices=[("furn <100", " <$100"), ("furn 100 - 300", "$100 - $300"),
                                                            ("furn >300", ">$300")])
    com_service = SelectField("Communication Services (Mobile phone, internet services, and postage):",
                              [validators.input_required],
                              choices=[("cs <40", "<$40"), ("cs 40 - 200", "$40 - $200"),
                                       ("cs >200", ">$200")])
    ed_service = SelectField("Educational Services:",
                              [validators.input_required],
                              choices=[("eds <100", "<$100"), ("eds 100 - 200", "$100 - $200"),
                                       ("eds >200", ">$200")])
    others = SelectField("Other Purchased Goods and Services (Laundry, haircut, insurance, alcoholic beverages and tobacco):",
                              [validators.input_required],
                              choices=[("o 0", "<$0"), ("o <120", "<$120"),
                                       ("o 120 - 500", "$120 - $500"), ("o >500", ">$500")])
    mrt_lrt = IntegerField("MRT/LRT (min)", [validators.input_required])
    bus = IntegerField("Bus (min)", [validators.input_required])
    ride_services = IntegerField("Ride-hailing services (Taxi, Grab, Gojek, etc) (min)", [validators.input_required])
    motorcycle = IntegerField("Motorcycle (min)", [validators.input_required])
    drive_ride_passenger = IntegerField("Drive or ride as a passenger in a car (min)", [validators.input_required])
    sea = IntegerField("Southeast Asia", [validators.input_required])
    ap = IntegerField("Asia Pacific", [validators.input_required])
    ea = IntegerField("Europe/Africa", [validators.input_required])
    oc = IntegerField("Oceania", [validators.input_required])
    am = IntegerField("Americas", [validators.input_required])
    travel_class = SelectField("Which travel class do you usually travel in?",
                              [validators.input_required],
                              choices=[("tc b/e", "Budget/Economy"), ("tc pe", "Premium Economy"),
                                       ("tc b", "Business"), ("tc f", "First")])
    night_staycation = IntegerField(">How many nights of staycation did you take in this month?", [validators.input_required])