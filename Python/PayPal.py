from payment import Payment
class PayPal(Payment):
    reference = str
    sucursal = str

    #ahora construyo la herenciaa.
    def __init__(self, id, reference, sucursal) -> None:
        super().__init__(id)
        self.reference = reference
        self.sucursal = sucursal