from car import Car

class UberPool(Car):
    brand = str
    model = str

    #Se declara la herencia de la familia car
    def __init__(self, license, driver, bramd, model) -> None:
        super().__init__(license, driver)
        self.brand = bramd
        self.model = model