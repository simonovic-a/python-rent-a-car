
from models.User import User
from models.User import users
from models.Car import Car


print("1. Add user\n"
      "2. Show users\n"
      "3. Show available vehicles\n"
      "4. Show rented vehicles")

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
        for user in users:
            print(user)
        option = None

    elif option == 3 or option == 4:
        for brand in Car.VALID_CARS:
            for car in Car.VALID_CARS[brand]:
                if not car["rented"] and option == 3:
                    print(car)
                elif car["rented"] and option == 4:
                    print(car)
        option = None
