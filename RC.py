import threading

from models.TimeConductor import TimeConductor
from sensor.DataLogger import DataLogger

tc = TimeConductor()
dl = DataLogger()


thread_logger = threading.Thread(target=dl.log)
thread_logger.daemon = True
thread_logger.start()

tc.runActuator()
print('finish safely')


