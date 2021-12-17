from account import Account

class Car:
    id          = int
    license     = str
    driver      = Account("", "")
    passenger   = int

    # Creaación del método constructor
    def __init__(self, license, driver) -> None:
        self.license    = license
        self.driver     = driver
