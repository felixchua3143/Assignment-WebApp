#from User import *
class CarbonForm():
    def __init__(self, user_id, num_household, electricity, gas, water, food, cloth_footwear, recreate_act,
                 furn_house_equipment_maintenance, com_service, ed_service, others, mrt_lrt, bus, ride_services,
                 motorcycle, drive_ride_passenger, sea, ap, ea, oc, am, travel_class, night_staycation):
        #super().__init__(user_id = 1, first_name = "abc")
        self.__user_id = user_id
        self.__num_household = num_household
        self.__electricity = electricity
        self.__gas = gas
        self.__water = water
        self.__food = food
        self.__cloth_footwear = cloth_footwear
        self.__recreate_act = recreate_act
        self.__furn_house_equipment_maintenance = furn_house_equipment_maintenance
        self.__com_service = com_service
        self.__ed_service = ed_service
        self.__others = others
        self.__mrt_lrt = mrt_lrt
        self.__bus = bus
        self.__ride_services = ride_services
        self.__motorcycle = motorcycle
        self.__drive_ride_passenger = drive_ride_passenger
        self.__sea = sea
        self.__ap = ap
        self.__ea = ea
        self.__oc = oc
        self.__am = am
        self.__travel_class = travel_class
        self.__night_staycation = night_staycation

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_num_household(self):
        return self.__num_household

    def set_num_household(self, num_household):
        self.__num_household = num_household

    def get_electricity(self):
        return self.__electricity

    def set_electricity(self, electricity):
        self.__electricity = electricity

    def get_gas(self):
        return self.__gas

    def set_gas(self, gas):
        self.__gas = gas

    def get_water(self):
        return self.__water

    def set_water(self, water):
        self.__water = water

    def get_food(self):
        return self.__food

    def set_food(self, food):
        self.__food = food

    def get_cloth_footwear(self):
        return self.__cloth_footwear

    def set_cloth_footwear(self, cloth_footwear):
        self.__cloth_footwear = cloth_footwear

    def get_recreate_act(self):
        return self.__recreate_act

    def set_recreate_act(self, recreate_act):
        self.__recreate_act = recreate_act

    def get_furn_house_equipment_maintenance(self):
        return self.__furn_house_equipment_maintenance

    def set_furn_house_equipment_maintenance(self, furn_house_equipment_maintenance):
        self.__furn_house_equipment_maintenance = furn_house_equipment_maintenance

    def get_com_service(self):
        return self.__com_service

    def set_com_service(self, com_service):
        self.__com_service = com_service

    def get_ed_service(self):
        return self.__ed_service

    def set_ed_service(self, ed_service):
        self.__ed_service = ed_service

    def get_others(self):
        return self.__others

    def set_others(self, others):
        self.__others = others

    def get_mrt_lrt(self):
        return self.__mrt_lrt

    def set_mrt_lrt(self, mrt_lrt):
        self.__mrt_lrt = mrt_lrt

    def get_bus(self):
        return self.__bus

    def set_bus(self, bus):
        self.__bus = bus

    def get_ride_services(self):
        return self.__ride_services

    def set_ride_services(self, ride_services):
        self.__ride_services = ride_services

    def get_motorcycle(self):
        return self.__motorcycle

    def set_motorcycle(self, motorcycle):
        self.__motorcycle = motorcycle

    def get_drive_ride_passenger(self):
        return self.__drive_ride_passenger

    def set_drive_ride_passenger(self, drive_ride_passenger):
        self.__drive_ride_passenger = drive_ride_passenger

    def get_sea(self):
        return self.__sea

    def set_sea(self, sea):
        self.__sea = sea

    def get_ap(self):
        return self.__ap

    def set_ap(self, ap):
        self.__ap = ap

    def get_ea(self):
        return self.__ea

    def set_ea(self, ea):
        self.__ea = ea

    def get_oc(self):
        return self.__oc

    def set_oc(self, oc):
        self.__oc = oc

    def get_am(self):
        return self.__am

    def set_am(self, am):
        self.__am = am

    def get_travel_class(self):
        return self.__travel_class

    def set_travel_class(self, travel_class):
        self.__travel_class = travel_class

    def get_night_staycation(self):
        return self.__night_staycation

    def set_night_staycation(self, night_staycation):
        self.__night_staycation = night_staycation
