from controller.run_motor import DCMotor

class Driving:
  def __init__(self):
    self.actuator = DCMotor()

  def forward(self, accelOpening):
    self.actuator.CW(accelOpening)

  def backward(self, accelOpening):
    self.actuator.CCW(accelOpening)

  def stop(self):
    self.actuator.stop()

  def actuate(self, data):
    accelPedal = data[0]
    breakPedal = data[1]
    if accelPedal > 0.9 and breakPedal > 0.9:
      self.stop()
    elif breakPedal < accelPedal:
      self.backward( (-breakPedal + 1) * 50)
    else:
      self.forward( (-accelPedal + 1) * 50 )
    return