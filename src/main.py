

from rocket.fuel_tank import FuelTank
from rocket.engine import Engine
from rocket.rocket import Rocket

fuel_tank = FuelTank(capacity=500.0)  # Create a fuel tank with a capacity of 500 kg

engine = Engine(max_thrust= 15000.0, specific_impulse=300.0)  # Create an engine with 15,000 N max thrust and 300 s specific impulse

rocket = Rocket(dry_mass=500.0, engine=engine, fuel_tank=fuel_tank)  # Create a rocket with a dry mass of 500 kg and total mass as 1000kg

rocket.engine.set_throttle(1.0)


#Testing

print(
    "Thrust:",
    rocket.engine.get_thrust()
)

print(
    "Mass Flow:",
    rocket.engine.get_mass_flow_rate()
)

print(
    "Fuel:",
    rocket.fuel_tank.fuel_mass
)

print(
    "Mass:",
    rocket.total_mass
)


# simulating for 1 sec

rocket.update_engine(1.0)

print(
    "Fuel:",
    rocket.fuel_tank.fuel_mass
)

print(
    "Mass:",
    rocket.total_mass
)
