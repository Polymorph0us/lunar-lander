from rocket.engine import Engine
from rocket.fuel_tank import FuelTank

class Rocket:
    def __init__(self,dry_mass:float,engine:Engine,fuel_tank:FuelTank):
        self.dry_mass = dry_mass
        self.engine = engine
        self.fuel_tank = fuel_tank
        self.position = [0.0,1000.0]
        self.velocity = [0.0,0.0]
        self.altitude = 0.0

    @property
    def total_mass(self):
        return self.dry_mass + self.fuel_tank.fuel_mass

    def update_engine(self,dt:float):

        if self.fuel_tank.is_empty():
            self.engine.set_throttle(0.0)
            return
        
        mass_flow_rate = self.engine.get_mass_flow_rate()

        fuel_needed = mass_flow_rate * dt  

        self.fuel_tank.consume(fuel_needed)

    def get_thrust(self):
        return self.engine.get_thrust()

   