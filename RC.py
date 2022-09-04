import os
from dotenv import load_dotenv
from models.TimeConductor import TimeConductor
from communication import UDP_recieve, UDP_transmit
from models.Driving import Driving
from models.Steering import Steering
from sensor.Camera import Camera
import threading

load_dotenv('./.env')

class RC:
  def __init__(self):
    IP = os.getenv('MY_PC_OMEN')
    # IP = "127.0.0.1"
    self.tc_recv = TimeConductor(sampling_time=0)
    self.tc_trans = TimeConductor(sampling_time=0)
    self.reciever = UDP_recieve.udprecv()
    self.transmitter = UDP_transmit.udptrans(IP=IP)
    self.driving = Driving()
    self.steering = Steering()
    # self.camera = Camera(FPS=30)

  def runActuator(self, data):
    self.driving.actuate([data[1], data[2]])
    self.steering.actuate(data[0])

  def transmitSensor(self, frame):
    # self.transmitter.transmit_img(frame, quality=30)
    return

  def serving_recv(self):
    data = self.reciever.receive_digits() # 0:steering, 1:accel, 2:break
    self.runActuator(data)

  def serving_trans(self):
    # frame = self.camera.capture()
    # self.transmitSensor(frame)
    return

  def close_recv(self):
    self.driving.stop()
    self.steering.stop()
    self.reciever.socketClose()

  def close_trans(self):
    # self.camera.close()
    self.transmitter.socketClose()

  def serve(self):
    print('start serving')
    th_trans = threading.Thread(target=self.tc_trans.conduct, args=(self.serving_trans, self.close_trans, ))
    th_trans.daemon = True
    th_trans.start()

    self.tc_recv.conduct(self.serving_recv, self.close_recv)
    self.tc_trans.isConducting = False

if __name__ == '__main__':
  rc = RC()
  rc.serve()
  print('finish safely')
