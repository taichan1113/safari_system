from controller.run_servo_hardware import Servo

class Steering:
  def __init__(self):
    self.gear_ratio = -90.0 # ratio from data to servo
    self.actuator = Servo()
#     self.actuator.init()

  def actuate(self, data):
    angle = data * self.gear_ratio
    self.actuator.setAngle(angle)
