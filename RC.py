from communication import UDP_recieve, UDP_transmit
from models.Driving import Driving
from models.Steering import Steering
from sensor.Camera import Camera
import threading

from models.TimeConductor import TimeConductor
# from sensor.DataLogger import DataLogger

class RC:
  def __init__(self):
    IP = "192.168.11.11"
    # IP = "127.0.0.1"
    sampling_time = 0.05
    self.tc = TimeConductor(sampling_time=sampling_time)

    self.reciever = UDP_recieve.udprecv()
    self.transmitter = UDP_transmit.udptrans(IP)
    self.driving = Driving()
    self.steering = Steering()
    self.camera = Camera(1/sampling_time)

  def conduct(self):
    event = threading.Event()
    th_actuator = threading.Thread(target=self.tc.timeKeeper, args=(self.runActuatorOnce, self.stopActuator, ))
    th_sensor = threading.Thread(target=self.tc.timeKeeper, args=(self.transmitSensorOnce, self.closeSensor, ))
    th_stopListner = threading.Thread(target=self.stopListening, args=(event, ))

    self.tc.isConducting = True

    th_stopListner.start()
    th_actuator.start()
    th_sensor.start()
    try:
      while True:
        continue
    except KeyboardInterrupt:
      event.set()
      th_actuator.join()
      th_sensor.join()
      th_stopListner.join()
      print('finish safely')

  def stopListening(self, event):
    event.wait()
    self.tc.isConducting = False

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


# dl = DataLogger()
# dl.isLogging = True
# 
# thread_logger = threading.Thread(target=dl.log)
# thread_logger.daemon = True
# thread_logger.start()
# dl.isLogging = False

if __name__ == '__main__':
  rc = RC()
  rc.conduct()