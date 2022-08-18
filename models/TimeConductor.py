import time
from communication import UDP_recieve, UDP_transmit
from models.Driving import Driving
from models.Steering import Steering
from sensor.Camera import Camera

class TimeConductor:
  def __init__(self):
    IP = "192.168.11.11"
    # IP = "127.0.0.1"
    self.sampling_time = 0.1
    self.reciever = UDP_recieve.udprecv()
    self.transmitter = UDP_transmit.udptrans(IP)
    self.now = None

  def runActuator(self):
    print("Actuator running")
    driving = Driving()
    steering = Steering()
    self.now = time.time()
    try:
      while True:
        if time.time() - self.now < self.sampling_time:
          continue
        self.now = time.time()
        data = self.reciever.receive_digits() # 0:steering, 1:accel, 2:break
        driving.actuate([data[1], data[2]])
        steering.actuate(data[0])
    except KeyboardInterrupt:
      driving.stop()
      steering.stop()
    
  def transmitSensor(self):
    print("Sensor transmitting")
    FPS = 1/self.sampling_time
    camera = Camera(FPS)
    try:
      while True:
        frame = camera.capture()
        if not frame:
          break
        self.transmitter.transmit_img(frame, 20)
        
    except KeyboardInterrupt:
      camera.close()
      self.transmitter.udpClntSock.close()

if __name__ == '__main__':
  tc = TimeConductor()
  tc.runActuator()