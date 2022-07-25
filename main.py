
from account import Account
from car import Car
from cash import Cash
from uberConfort import UberConfort
from uberX import UberX


if __name__ == "__main__":
    print ("Hola Mundo!")
    
    
    car = Car("PBO6555", Account("Ismael Andrade", "1720635210"))
    print (vars(car))
    print (vars(car.driver))
    
    uberX = UberX("PCC-1234", Account("Ismael Andrade", "1720635210"), "Chevrolet", "Spark")
    print (vars(uberX))
    
    uberConfort = UberConfort("JIC-2020", Account("Ismael Andrade", "1720635210"), "Dodge", "Cuero", "6")
    print (vars(uberConfort))
    print (vars(uberConfort.driver))
    
    pagoDinero = Cash("1", "14-7-2022", "20", "Cash")
    print(vars(pagoDinero))
    print(pagoDinero.date)
    