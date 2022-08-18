import time
from communication import UDP_recieve, UDP_transmit
from models.Driving import Driving
from models.Steering import Steering
from sensor.Camera import Camera
import threading

class TimeConductor:
  def __init__(self):
    IP = "192.168.11.11"
    # IP = "127.0.0.1"
    self.sampling_time = 0.05
    self.now = None
    self.isConducting = False

    self.reciever = UDP_recieve.udprecv()
    self.transmitter = UDP_transmit.udptrans(IP)
    self.driving = Driving()
    self.steering = Steering()
    self.camera = Camera(1/self.sampling_time)

  def conduct(self):
    event = threading.Event()
    th_actuator = threading.Thread(target=self.timeKeeper, args=(self.runActuatorOnce, self.stopActuator, ))
    th_sensor = threading.Thread(target=self.timeKeeper, args=(self.transmitSensorOnce, self.closeSensor, ))
    th_stopListner = threading.Thread(target=self.stopListening, args=(event, ))

    self.isConducting = True

    th_stopListner.start()
    th_actuator.start()
    th_sensor.start()
    while True:
      try:
        continue
      except KeyboardInterrupt:
        break
    event.set()

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

  def stopListening(self, event):
    event.wait()
    self.isConducting = False

  def runActuatorOnce(self):
    data = self.reciever.receive_digits() # 0:steering, 1:accel, 2:break
    self.driving.actuate([data[1], data[2]])
    self.steering.actuate(data[0])

  def stopActuator(self):
    self.driving.stop()
    self.steering.stop()
    self.reciever.udpServSock.close()

  def transmitSensorOnce(self):
    frame = self.camera.capture()
    self.transmitter.transmit_img(frame, 20)

  def closeSensor(self):
    self.camera.close()
    self.transmitter.udpClntSock.close()

if __name__ == '__main__':
  tc = TimeConductor()
  # tc.runActuatorOnce()