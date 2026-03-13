from Db import Db

class User(Db):

    def __init__(self):
        super().__init__()
        con = self._get_connection()
        print(con)


    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age < 18:
            raise ValueError("Morate imati minimum 18 godina")
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) < 3:
            raise ValueError("Ime mora imati bar 3 karaktera")
        self.__name = name
