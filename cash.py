from payment import Payment

class Cash(Payment):
    
    def __init__(self, id, date, ammount, typePayment):
        super().__init__(id, ammount, date, typePayment)