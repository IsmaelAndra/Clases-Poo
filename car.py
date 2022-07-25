from account import Account

class Car:
    id          = int
    driver      = Account("","")
    passanggers = int
    license     = str

    def __init__(self, license, driver):
        self.license    = license
        self.driver     = driver  