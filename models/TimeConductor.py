import time

class TimeConductor:
  def __init__(self, sampling_time=0.05):
    self.sampling_time = sampling_time
    self.now = None

  def conduct(self, conduct_handler, finish_handler):
    print('start conduct')
    # self.now = time.time()
    try:
      while True:
        # if time.time() - self.now < self.sampling_time:
        #   continue
        conduct_handler()
        time.sleep(self.sampling_time)
        # self.now = time.time()

    except KeyboardInterrupt:
      finish_handler()
      print('finish conduct')
