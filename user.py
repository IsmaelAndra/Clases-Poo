
from account import Account


class User(Account):
    idUser = int
    
    def __init__(self, idUser, name, document, mail, password, gender, numberCell, age):
        super().__init__(name, document, mail, password, gender, numberCell, age)
        self.idUser    = idUser
        
                 