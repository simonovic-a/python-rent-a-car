from models.Car import Car
from models.User import User

print("1. Add user\n"
      "2. Show all users\n"
      "3. Show available vehicles\n"
      "4. Show rented vehicles\n"
      "5. Add car\n"
      "6. Rent car\n"
      "7. Return car")

available_options = [1, 2, 3, 4]
option = None

while option is None or option not in available_options:
    option = int(input("Choose an option: "))

    if option == 1:
        user = User()
        user.name = input("Input users full name: ")
        user.age = int(input("Input users age: "))
        user.create()
        option = None

    elif option == 2:
        user = User()
        users = user.get_all_users()
        for user in users:
            print(f"Id: {user["id"]} | Name: {user["name"]} | Age: {user["age"]}")
        option = None

    elif option == 3 or option == 4:
        car_obj = Car()
        cars = car_obj.all_cars()

        for car in cars:
            if not car["rented"] and option == 3:
                print(f'Id: {car["id"]} | {car["brand"]} {car["model"]} {car["production_year"]}')

            elif car["rented"] and option == 4:
                remaining = car_obj.time_left(car["rented_until"])

                print(
                    f'Car ID: {car["id"]} | {car["brand"]} {car["model"]} {car["production_year"]} | User ID: {car["user_id"]} | Remaining: {remaining}')

    elif option == 5:
        car = Car()
        car.brand = input("Enter car brand: ")
        car.model = input("Enter car model: ")
        car.production_year = input("Enter car production year: ")
        car.create()

        option = None

    elif option == 6:
        car = Car()
        car_id = input("Enter car ID: ")
        user_id = input("Enter user ID: ")
        rent_date = input("Enter rental end date (YYYY-MM-DD HH:MM:SS): ")
        car.rent_car(car_id, user_id, rent_date)

        option = None

    elif option == 7:
        car = Car()
        car_id = input("Enter car ID: ")
        car.return_car(car_id)

        option = None