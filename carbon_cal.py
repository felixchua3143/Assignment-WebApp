from User import *


class Carbon_Cal(User):
    def __init__(self, electricity, gas, water, num_household):
        super().__init__(user_id=999, first_name="abc")
        self.electricity = electricity
        self.gas = gas
        self.water = water
        self.num_household = num_household
