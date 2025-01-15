# User class
class User:
    count_id = 0

    # initializer method
    def __init__(self, electricity, num_household,water, gas, food):
        User.count_id += 1
        self.__user_id = User.count_id
        self.__electricity = electricity
        self.__num_household = num_household
        self.__water = water
        self.__gas = gas
        self.__food = food

    # accessor methods
    def get_user_id(self):
        return self.__user_id

    def get_num_household(self):
        return self.__num_household

    def get_electricity(self):
        return self.__electricity

    def get_water(self):
        return self.__water

    def get_gas(self):
        return self.__gas

    def get_food(self):
        return self.__food

    # mutator methods
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_num_household(self, num_household):
        self.__num_household = num_household

    def set_electricity(self, electricity):
        self.__electricity = electricity

    def set_water(self, water):
        self.__water = water

    def set_gas(self, gas):
        self.__gas = gas

    def set_food(self, food):
        self.__food = food
