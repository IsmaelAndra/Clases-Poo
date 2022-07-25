from car import Car


class UberConfort(Car):
    numberPassanggers     = int
    carAccepted           = []
    seatMaterial          = []
    
    def __init__(self, license, driver, carAccepted, seatMaterial, numberPassanggers):
        super().__init__(license, driver)
        self.carAccepted        = carAccepted
        self.seatMaterial       = seatMaterial
        self.numberPassanggers  = numberPassanggers