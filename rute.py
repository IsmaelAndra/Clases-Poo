class Rute():
    start          = []
    end            = []
    kmDistance     = int
    timeAprox      = int
    payAprox       = float
    
    def __init__(self, start, end, kmDistance, timeAprox, payAprox):
        self.start      = start
        self.end        = end
        self.kmDistance = kmDistance
        self.timeAprox  = timeAprox
        self.payAprox   = payAprox