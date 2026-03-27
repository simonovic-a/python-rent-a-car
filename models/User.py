from models.Db import Db


class User(Db):

    def __init__(self):
        super().__init__()
        self.__name = None
        self.__age = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        split_name = new_name.split()
        if len(split_name) < 2:
            raise ValueError("Name must contain first and last name.")

        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("You must be 18 years old.")
        self.__age = age

    def get_all_users(self):
        con = self._get_connection()
        cursor = con.cursor()

        cursor.execute("SELECT id, name, age FROM users")
        users = cursor.fetchall()

        cursor.close()

        return users

    def create(self):
        con = self._get_connection()
        cursor = con.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (self.__name, self.__age))
        con.commit()
        cursor.close()
        print("Successfully created new user.")
