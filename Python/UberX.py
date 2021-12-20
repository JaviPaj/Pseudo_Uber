from car import Car

class UberX(Car):
    brand = str
    model = str

    #Ahora se indica la herencia a la familia car
    def __init__(self, license, driver, brand, model) -> None:
        super().__init__(license, driver)
        self.brand = brand
        self.model = model