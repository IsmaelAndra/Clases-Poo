from bank import Bank


class Transfer(Bank):
    
   def __init__(self, id, typePayment, ammount, date, bankName, identification, numberAccount):
      super().__init__(id, typePayment, ammount, date, bankName, identification, numberAccount)