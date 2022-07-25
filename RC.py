import threading

from models.TimeConductor import TimeConductor
from sensor.DataLogger import DataLogger

tc = TimeConductor()
dl = DataLogger()

thread_system = threading.Thread(target=tc.runActuator())
thread_logger = threading.Thread(target = dl.log())
thread_system.run()
thread_logger.run()
# tc.runActuator()
