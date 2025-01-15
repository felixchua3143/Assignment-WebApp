class User:
    def __init__(self, new_id, user_type, name):
        self.__id = new_id
        self.__user_type = user_type
        self.__name = name

    def set_user_id(self, _id):
        self.__id = _id

    def set_user_type(self, user_type):
        self.__user_type = user_type

    def set_user_name(self, name):
        self.__name = name

    def get_user_id(self):
        return self.__id

    def get_user_type(self):
        return self.__user_type

    def get_user_name(self):
        return self.__name
