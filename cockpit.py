import pygame
from pygame.locals import *
from communication import UDP_recieve, UDP_transmit
import cv2
import time
from dotenv import load_dotenv
import os
import threading
from models.TimeConductor import TimeConductor

load_dotenv('./.env')
IP = os.getenv('MY_RASPIZERO2_IP')

class UI:
  def __init__(self, type='handle controller'):
    sampling_time = 0.05
    self.tc = TimeConductor(sampling_time=sampling_time)

    self.recv = UDP_recieve.udprecv()
    self.trans = UDP_transmit.udptrans(IP)

    # pygame初期化
    pygame.init()
    self.joystick = pygame.joystick.Joystick(0)
    self.joystick.init()
    self.showJoystickInfo()
    
    # コントローラータイプ
    self.type = type

  def conduct(self):
    event = threading.Event()
    th_data = threading.Thread(target=self.tc.timeKeeper, args=(self.transmitDataOnce, self.stopData, ))
    th_camera = threading.Thread(target=self.tc.timeKeeper, args=(self.showCaptureOnce, self.endCapture, ))
    th_stopListner = threading.Thread(target=self.stopListening, args=(event, ))

    self.tc.isConducting = True

    th_stopListner.start()
    th_data.start()
    th_camera.start()
    try:
      while True:
        continue
    except KeyboardInterrupt:
      event.set()
      th_data.join()
      th_camera.join()
      th_stopListner.join()
      print('finish safely')

  def stopListening(self, event):
    event.wait()
    self.tc.isConducting = False

  def showJoystickInfo(self):
    print(f'ジョイスティック名前: {self.joystick.get_name()}')
    print(f'ボタン数: {self.joystick.get_numbuttons()}')
    print(f'ジョイスティック軸数: {self.joystick.get_numaxes()}')

  def getSignal(self):
    # [steering, accelaration, brake]
    if self.type == 'handle controller':
      return [self.joystick.get_axis(0), self.joystick.get_axis(1), self.joystick.get_axis(2)]
    elif self.type == 'joystick controller':
      return [self.joystick.get_axis(0), -self.joystick.get_axis(5), -self.joystick.get_axis(4)]
    else:
      return [0, 0]

  def printSignal(self, e):
    if e.type == pygame.locals.JOYAXISMOTION:
      print('ジョイスティック:', self.getSignal())
    elif e.type == pygame.locals.JOYBUTTONDOWN:
      print(f'ボタン{e.button}を押した')
    elif e.type == pygame.locals.JOYBUTTONUP:
      print(f'ボタン{e.button}を離した')

  def transmitSignal(self, e):
    if e.type == pygame.locals.JOYAXISMOTION:
      self.trans.transmit_digits(self.getSignal())

  def showCaptureOnce(self):
    img = self.recv.receive_img()
    cv2.imshow('result', img)
    cv2.waitKey(int(self.tc.sampling_time*1000)) # sec to msec
    
  def endCapture(self):
    cv2.destroyAllWindows()
    self.recv.udpServSock.close()
    print('stop camera')

  def transmitDataOnce(self):
    for e in pygame.event.get():
      if e.type == QUIT:
        break
      # self.printSignal(e)
      self.transmitSignal(e)

  def stopData(self):
    print('stop run')

    
if __name__ == "__main__":
  ui = UI(type='joystick controller')
  ui.conduct()