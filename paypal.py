from payment import Payment


class Paypal(Payment):
    id      = int
    email   = str
    
    def __init__(self, id, email, ammount):
        super.__init__(id, email, ammount)
        super.id = id
        super.email = email