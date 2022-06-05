import time
from communication import UDP_recieve
from models.Steering import Steering

class TimeConductor:
  def __init__(self):
    self.sampling_time = 0.1
    self.reciever = UDP_recieve.udprecv()
    self.now = None

  def runSystem(self):
    print("system running")
    steering = Steering()
    self.now = time.time()
    while True:
      if time.time() - self.now < self.sampling_time:
        continue
      self.now = time.time()
      data = self.reciever.receive_digits()
      steering.actuate(data[0], self.sampling_time)

if __name__ == '__main__':
  tc = TimeConductor()
  tc.runSystem()