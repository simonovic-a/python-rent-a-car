from datetime import datetime

from models.Db import Db

class Car(Db):

    def __init__(self):
        super().__init__()
        self.__brand = None
        self.__model = None
        self.__production_year = None

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand


    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__brand is None:
            raise ValueError("Brand must be set.")
        self.__model = model

    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self, production_year):
        if self.model is None:
            raise ValueError("Model must be set.")
        self.__production_year = production_year

    def create(self):
        con = self._get_connection()
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO cars (brand, model, production_year, rented, user_id, rented_until) VALUES (%s, %s, %s, %s, %s, %s)",
            (self.__brand, self.__model, self.__production_year, False, None ,None)
        )
        con.commit()
        cursor.close()
        print("Successfully added new car.")

    def all_cars(self):
        con = self._get_connection()
        cursor = con.cursor()

        cursor.execute("SELECT id, brand, model, production_year, rented, user_id, rented_until FROM cars")
        cars = cursor.fetchall()

        con.commit()
        cursor.close()
        return cars

    def rent_car(self, car_id, user_id, rent_date):
        rented_until = datetime.strptime(rent_date, "%Y-%m-%d %H:%M:%S")

        con = self._get_connection()
        cursor = con.cursor()

        cursor.execute("UPDATE cars SET rented = %s, user_id = %s, rented_until = %s WHERE id = %s AND rented = %s",
                       (True, user_id, rented_until, car_id, False))
        con.commit()
        cursor.close()
        print(f"Car with ID {car_id} has been successfully rented.")

    def return_car(self, car_id):
        con = self._get_connection()
        cursor = con.cursor()

        cursor.execute(
            "UPDATE cars SET rented = %s, user_id = %s, rented_until = %s WHERE id = %s and rented = %s",
            (False, None, None, car_id, True)
        )

        con.commit()

        if cursor.rowcount == 0:
            print("Car is not rented or does not exist.")
        else:
            print(f"Car with ID {car_id} has been successfully returned.")

        cursor.close()

    def time_left(self, rented_until):
        now = datetime.now()
        diff = rented_until - now

        total_seconds = diff.total_seconds()

        if total_seconds <= 0:
            return "Expired"

        days = int(total_seconds // (24 * 3600))

        if days >= 1:
            return f"{days} day(s)"
        else:
            hours = int(total_seconds // 3600)
            return f"{hours} hour(s)"