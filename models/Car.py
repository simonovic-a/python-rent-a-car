class Car:
    VALID_CARS = {
        "Audi": [
            {"model": "A4", "production_year": 2004},
            {"model": "A5", "production_year": 2005},
            {"model": "A6", "production_year": 2006},
        ],
        "BMW": [
            {"model": "M3", "production_year": 2012},
            {"model": "M4", "production_year": 2018},
            {"model": "M5", "production_year": 2021},
        ]
        ,
        "Mercedes": [
            {"model": "GLK", "production_year": 2015},
            {"model": "GLE", "production_year": 2017},
            {"model": "GLC", "production_year": 2019},
        ]
    }

    def __init__(self):
        self.__brand = None
        self.__model = None
        self.__production_year = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__brand is None:
            raise ValueError("Brand must be set.")

        valid_models = []
        for car in Car.VALID_CARS[self.__brand]:
            valid_models.append(car['model'])

        if model not in valid_models:
            raise ValueError("Invalid model")
        self.__model = model

        for car_model in Car.VALID_CARS[self.__brand]:
            if car_model["model"] == self.__model:
                self.__production_year = car_model["production_year"]

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        if brand not in Car.VALID_CARS:
            raise ValueError("Invalid Car")

        self.__brand = brand

    @property
    def production_year(self):
        return self.__production_year

    @production_year.setter
    def production_year(self, year):
        if self.__model is None:
            raise ValueError("Production year cannot be set.")

        if self.__model is not None and self.__production_year is not None:
            raise ValueError("Production year cannot be set")
