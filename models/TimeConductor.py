import time

class TimeConductor:
  def __init__(self, sampling_time=0.05):
    self.sampling_time = sampling_time
    self.now = None
    self.isConducting = False

  def timeKeeper(self, executeHandler, stopHandler):
    print('start time keep')
    self.now = time.time()
    while self.isConducting:
      if time.time() - self.now < self.sampling_time:
        continue
      self.now = time.time()
      executeHandler()

    stopHandler()
    print('finish time keep')

if __name__ == '__main__':
  tc = TimeConductor()
  # tc.runActuatorOnce()