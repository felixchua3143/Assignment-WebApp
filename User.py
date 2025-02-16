from flask_login import UserMixin
class User(UserMixin):
    def __init__(self, id, username, password):
        self.__id = id
        self.__username = username
        self.__password = password

    def set_id(self, id):
        self.__id = id

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password
    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

