import time
from communication import UDP_recieve, UDP_transmit
from models.Driving import Driving
from models.Steering import Steering
from sensor.Camera import Camera

class TimeConductor:
  def __init__(self):
    IP = "192.168.11.11"
    # IP = "127.0.0.1"
    self.sampling_time = 0.05
    self.reciever = UDP_recieve.udprecv()
    self.transmitter = UDP_transmit.udptrans(IP)
    self.now = None
    self.isConducting = False

  def conduct(self):
    FPS = 1/self.sampling_time
    self.driving = Driving()
    self.steering = Steering()
    self.camera = Camera(FPS)

    self.now = time.time()
    self.isConducting = True

    print('start conduct')

    try:
      while self.isConducting:
        if time.time() - self.now < self.sampling_time:
          continue
        self.now = time.time()
        # receive and run actuator
        data = self.reciever.receive_digits() # 0:steering, 1:accel, 2:break
        self.runActuator(data)
        # get sensor and transmit
        frame = self.camera.capture()
        self.transmitSensor(frame)

    except KeyboardInterrupt:
      self.driving.stop()
      self.steering.stop()
      self.camera.close()
      self.reciever.udpServSock.close()
      self.transmitter.udpClntSock.close()
      self.isConducting = False
      print('finish conduct')

  def runActuator(self, data):
    self.driving.actuate([data[1], data[2]])
    self.steering.actuate(data[0])

  def transmitSensor(self, frame):
    self.transmitter.transmit_img(frame, 20)

if __name__ == '__main__':
  tc = TimeConductor()
  tc.runActuator()