class FuelTank:

    def __init__(self, capacity):
        self.capacity = capacity
        self.fuel_mass = capacity

    def consume(self,mass:float)-> float:
        consumed = min(mass, self.fuel_mass)
        self.fuel_mass -= consumed

        return consumed

    def is_empty(self)-> bool:
        return self.fuel_mass <= 0.0