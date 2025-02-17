class Carbon_Cal():
    def __init__(self, id, username, electricity, gas, water, num_household):
        super().__init__(id, username)
        self.electricity = electricity
        self.gas = gas
        self.water = water
        self.num_household = num_household

    def set_food(self, food):
       self.food = food

    def set_cloth_foot(self, cloth_foot):
        self.cloth_foot = cloth_foot

    def set_recreate_act(self, recreate_act):
        self.recreate_act = recreate_act

    def set_furn_house_ep_m(self, furn_house_ep_m):
        self.furn_house_ep_m = furn_house_ep_m

    def set_health(self, health):
        self.health = health

    def set_com_service(self, com_service):
        self.com_service = com_service

    def set_edu_service(self, edu_service):
        self.edu_service = edu_service

    def set_others(self, others):
        self.others = others

    def get_food(self):
        return self.food

    def get_cloth_foot(self):
        return self.cloth_foot
    def get_recreate_act(self):
        return self.recreate_act
    def get_furn_house_ep_m(self):
        return self.furn_house_ep_m
    def get_health(self):
        return self.health
    def get_com_service(self):
        return self.com_service
    def get_edu_service(self):
        return self.edu_service
    def get_others(self):
        return self.others