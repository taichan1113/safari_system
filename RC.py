from models.TimeConductor import TimeConductor
from communication import UDP_recieve, UDP_transmit
from models.Driving import Driving
from models.Steering import Steering
from sensor.Camera import Camera
import time

class RC:
  def __init__(self):
    IP = "192.168.11.11"
    # IP = "127.0.0.1"
    self.tc = TimeConductor()
    self.reciever = UDP_recieve.udprecv(blocking=False)
    self.transmitter = UDP_transmit.udptrans(IP)
    self.driving = Driving()
    self.steering = Steering()
    self.camera = Camera(FPS=int(1/self.tc.sampling_time))

  def runActuator(self, data):
    self.driving.actuate([data[1], data[2]])
    self.steering.actuate(data[0])

  def transmitSensor(self, frame):
    self.transmitter.transmit_img(frame, quality=20)

  def serving(self):
    data = self.reciever.receive_digits() # 0:steering, 1:accel, 2:break
    self.runActuator(data)
    frame = self.camera.capture()
    self.transmitSensor(frame)
    
  def close(self):
    self.driving.stop()
    self.steering.stop()
    self.camera.close()
    self.reciever.socketClose()
    self.transmitter.socketClose()
    print('closed')

  def serve(self):
    print('start serving')
    self.tc.conduct(self.serving, self.close)

if __name__ == '__main__':
  rc = RC()
  rc.serve()
  print('finish safely')

# from models.TimeConductor import TimeConductor

# tc = TimeConductor()
# dl = DataLogger()
# dl.isLogging = True
# 
# thread_logger = threading.Thread(target=dl.log)
# thread_logger.daemon = True
# thread_logger.start()

# tc.conduct()
# dl.isLogging = False
