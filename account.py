class Account() :
    id          = int
    name        = str
    document    = str
    mail        = str
    password    = str
    gender      = str
    numberCell  = int
    age         = int
    
    #Metodo Constructor en Python
    def __init__(self, name, document):
        self.name       = name
        self.document   = document
        