import threading

from models.TimeConductor import TimeConductor
from sensor.DataLogger import DataLogger

tc = TimeConductor()
# dl = DataLogger()
# dl.isLogging = True
# 
# thread_logger = threading.Thread(target=dl.log)
# thread_logger.daemon = True
# thread_logger.start()

tc.runActuator()
# dl.isLogging = False
print('finish safely')
