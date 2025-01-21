from User import *


class Carbon_Cal(User):
    def __init__(self, electricity, gas, water, num_household, food, cloth_foot, recreate_act, furn_house_ep_m, health,
                 com_service, edu_service, others):
        #food, cloth_foot, recreate_act, furn_house_ep_m, health,
        #         com_service, edu_service, others
        #remove the attributes cut off at final form field of
        #utility consumption page (num_household)
        super().__init__(user_id=999, first_name="abc")
        self.electricity = electricity
        self.gas = gas
        self.water = water
        self.num_household = num_household
        self.food = food
        self.cloth_foot = cloth_foot
        self.recreate_act = recreate_act
        self.furn_house_ep_m = furn_house_ep_m
        self.health = health
        self.com_service = com_service
        self.edu_service = edu_service
        self.others = others

        #def set_food(self, food):
        #    self.food = food

        #def set_cloth_foot(self, cloth_foot):
        #    self.cloth_foot = cloth_foot
