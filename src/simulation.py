import time

from rocket.engine import Engine
from rocket.fuel_tank import FuelTank
from rocket.rocket import Rocket
from physics.physics_engine import PhysicsEngine


engine = Engine(
    max_thrust=2000,
    specific_impulse=300
)

fuel_tank = FuelTank(
    capacity=500
)

rocket = Rocket(
    dry_mass=500,
    fuel_tank=fuel_tank,
    engine=engine
)

physics = PhysicsEngine(
    dt=0.02
)


rocket.engine.set_throttle(1.0)  # Set throttle to full power

for i in range(1000):

    physics.step(rocket)

    print(
        f"Time: {i * 0.02:.2f}s | "
        f"Altitude: {rocket.position[1]:.2f}m | "
        f"Velocity: {rocket.velocity[1]:.2f}m/s | "
        f"Fuel: {rocket.fuel_tank.fuel_mass:.2f}kg"
    )

    time.sleep(0.02)

