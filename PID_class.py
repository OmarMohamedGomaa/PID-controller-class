class PIDController:

    def __init__(self, Kp, Ki, Kd, dt=0.1):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt

        self.target = 0.0
        self.feedback = 0.0

        self.error_integral = 0.0
        self.previous_error = 0.0

        self.deadzone = 0.0

    def set_target(self, target):
        self.target = target

    def update_feedback(self, feedback):
        self.feedback = feedback

    def set_deadzone(self, deadzone):
        self.deadzone = deadzone

    def compute(self):

        error = self.target - self.feedback

    
        if abs(error) < self.deadzone:
            error = 0.0

        self.error_integral += error * self.dt


        derivative = (error - self.previous_error) / self.dt


        output =  self.Kp * error + self.Ki * self.error_integral    + self.Kd * derivative
        

        self.previous_error = error

        return output