import threading

from models.TimeConductor import TimeConductor
from sensor.DataLogger import DataLogger

tc = TimeConductor()
dl = DataLogger()

# thread_system = threading.Thread(target=tc.runActuator)
# thread_logger = threading.Thread(target=dl.log)
# thread_logger.daemon = True
# thread_logger.start()

# thread_system.start()
# thread_logger.start()


tc.runActuator()
print('finish safely')


# dl.log()

