import time

class TimeConductor:
  def __init__(self, sampling_time=0.05):
    self.sampling_time = sampling_time

  def conduct(self, conduct_handler, finish_handler):
    print('start conduct')
    while True:
      try:
        conduct_handler()
        time.sleep(self.sampling_time)

      except KeyboardInterrupt:
        finish_handler()
        print('finish conduct')
        break
