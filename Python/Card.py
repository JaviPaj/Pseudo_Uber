from payment import Payment
from datetime import date

class Card(Payment):
    cardBank = str
    endDate = date.today()
    cvv = int

    def __init__(self, id, cardBank,endDate, cvv) -> None:
        super().__init__(id)
        self.cardBank = cardBank
        self.endDate = endDate
        self.cvv = cvv