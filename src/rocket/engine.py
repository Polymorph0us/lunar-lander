class Engine:

    #Initializing the engine with maximum thrust and specific impulse
    def __init__(self,max_thrust:float,specific_impulse:float):
        self.max_thrust = max_thrust
        self.specific_impulse = specific_impulse
        self.throttle = 0.0

    #Throttle is a value between 0 and 1, where 0 is no thrust and 1 is full thrust
    def set_throttle(self,throttle:float):
        self.throttle = max(0.0,min(1.0,throttle))

    # This function returns the current thrust of the engine based on the throttle setting
    def get_thrust(self):
        return self.max_thrust * self.throttle

    # This function returns the mass flow rate of the engine based on the current thrust and specific impulse
    def get_mass_flow_rate(self):
        g0 = 9.80665  
        return self.get_thrust() / (self.specific_impulse * g0)