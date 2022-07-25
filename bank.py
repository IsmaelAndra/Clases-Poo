from payment import Payment

class Bank(Payment):
    bankName        = str
    identification  = str
    numberAccount   = int
    
    def __init__(self, id, typePayment, ammount, date,  bankName, identification, numberAccount):
        super().__init__(id, typePayment, ammount, date)
        self.bankName       = bankName
        self.identification = identification
        self.numberAccount  = numberAccount