from car import Car

class UberVan(Car):
    typeCarAccepted = []
    seatsMaterial = []

    # La herencia de la familia car
    def __init__(self, license, driver, typeCarAccepted, seatsMaterial) -> None:
        super().__init__(license, driver)
        self.typeCarAccepted = typeCarAccepted
        self.seatsMaterial = seatsMaterial 