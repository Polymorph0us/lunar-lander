Moon_Gravity = 1.62  

class PhysicsEngine:
    def __init__(self,dt:float):
        self.dt = dt

    def calculate_acceleration(self,rocket):

        thrust = rocket.get_thrust()

        mass = rocket.total_mass

        gravitational_force = mass*Moon_Gravity

        net_force = thrust - gravitational_force

        acceleration = net_force/mass

        return acceleration

    def update_velocity(self, rocket):

        acceleration = self.calculate_acceleration(rocket)

        rocket.velocity[1] += acceleration * self.dt

    def update_position(self, rocket):

        rocket.position[1] += (
            rocket.velocity[1] * self.dt
        )

    def update_fuel(self, rocket):

        rocket.update_engine(self.dt)

    def step(self, rocket):

        rocket.update_engine(self.dt)

        self.update_velocity(rocket)

        self.update_position(rocket)

    