from account import Account

class Driver(Account):
    idDriver      = int
    license       = str
    
    def __init__(self, idDriver, license, name, document, mail, password, gender, numberCell, age):
        super().__init__(idDriver, name, document, mail, password, gender, numberCell, age)
        self.idDriver   = idDriver
        self.license    = license