class Account:
    id          = int
    name        = str
    document    = str
    email       = str
    password    = str

    # Creaación del método constructor
    def __init__(self, name, document) -> None:
        self.name       = name
        self.document   = document