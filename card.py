from bank import Bank


class Card(Bank):
    cardNumber        = int
    cardSecurityCode  = int
    cardDate          = int

    def __init__(self, id, ammount, typePayment, date, bankName, identification, numberAccount, cardNumber, cardDate, cardSecurityCode):
        super().__init__(id, ammount, typePayment, date, bankName, identification, numberAccount)
        self.cardDate           =   cardDate
        self.cardNumber         =   cardNumber
        self.cardSecurityCode   =   cardSecurityCode