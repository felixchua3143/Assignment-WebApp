class User:
    def __init__(self, user_id, first_name):
        self.__user_id = user_id
        self.__first_name = first_name

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id
    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name
