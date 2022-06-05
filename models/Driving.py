from controller.run_motor import DCMotor

class Driving:
  def __init__(self):
    self.actuator = DCMotor()

  def forward(self, accelOpening):
    self.actuator.drive(-accelOpening)

  def backward(self, accelOpening):
    self.actuator.back(-accelOpening)

  def stop(self):
    self.actuator.stop()

  def actuate(self, data):
    accelPedal = data[0]
    breakPedal = data[1]
    if breakPedal < 0.6:
      self.stop()
    else:
      self.forward( (-accelPedal + 1) * 50 )
    return