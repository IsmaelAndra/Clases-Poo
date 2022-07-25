
class Payment : 
    id              = int
    ammount         = int
    date            = str
    typePayment     = []
    
    def __init__(self, id, ammount, date, typePayment):
        self.ammount        = ammount
        self.id             = id
        self.date           = date
        self.typePayment    = typePayment