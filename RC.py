import threading

from models.TimeConductor import TimeConductor

tc = TimeConductor()
tc.runActuator()

# thread_system = threading.Thread(target=tc.runActuator())
# thread_system.run()
