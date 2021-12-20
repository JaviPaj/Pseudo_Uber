from account import Account
  
class User(Account):
  phoneNumber = int
  city        = str  
  
  def __init__(self, document, email, password, phonenumber, city):
    super().__init__(document, email, password)
    self.phoneNumber  = phoneNumber
    self.city         = city
  
