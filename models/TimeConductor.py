import time
from communication import UDP_recieve
from models.Driving import Driving
from models.Steering import Steering

class TimeConductor:
  def __init__(self):
    self.sampling_time = 0.1
    self.reciever = UDP_recieve.udprecv()
    self.now = None

  def runSystem(self):
    print("system running")
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
        

if __name__ == '__main__':
  tc = TimeConductor()
  tc.runSystem()