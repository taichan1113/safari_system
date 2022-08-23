import os
import cv2
import pygame
from pygame.locals import *
from dotenv import load_dotenv
from communication import UDP_recieve, UDP_transmit
from models.TimeConductor import TimeConductor
import threading

load_dotenv('./.env')

class UI:
  def __init__(self, type='handle controller'):
    IP = os.getenv('MY_RASPIZERO2_IP')
    self.type = type
    self.tc_recv = TimeConductor(sampling_time=0)
    self.tc_trans = TimeConductor(sampling_time=0.05)
    pygame.init()
    self.joystick = pygame.joystick.Joystick(0)
    self.joystick.init()
    self.printJoystickInfo()
    self.trans = UDP_transmit.udptrans(IP=IP)
    self.recv = UDP_recieve.udprecv(blocking=False)

  def printJoystickInfo(self):
    print(f'ジョイスティック名前: {self.joystick.get_name()}')
    print(f'ボタン数: {self.joystick.get_numbuttons()}')
    print(f'ジョイスティック軸数: {self.joystick.get_numaxes()}')

  def getSignal(self): # [steering, accelaration, brake]
    if self.type == 'handle controller':
      return [self.joystick.get_axis(0), self.joystick.get_axis(1), self.joystick.get_axis(2)]
    elif self.type == 'joystick controller':
      return [self.joystick.get_axis(0), -self.joystick.get_axis(5), -self.joystick.get_axis(4)]
    else:
      return [0, 0, 0]

  def printSignal(self, e):
    if e.type == pygame.locals.JOYAXISMOTION:
      print('ジョイスティック:', self.getSignal())
    elif e.type == pygame.locals.JOYBUTTONDOWN:
      print(f'ボタン{e.button}を押した')
    elif e.type == pygame.locals.JOYBUTTONUP:
      print(f'ボタン{e.button}を離した')

  def showCapture(self):
    try:
      img = self.recv.receive_img()
      cv2.imshow('result', img)
      cv2.waitKey(int(self.sampling_time*1000)) # sec to msec
    except:
      pass

  def running_trans(self):
    self.trans.transmit_digits(self.getSignal())
    pygame.event.clear()

  def running_recv(self):
    self.showCapture()

  def close_trans(self):
    self.trans.socketClose()
    print('closed')

  def close_recv(self):
    cv2.destroyAllWindows()
    self.recv.socketClose()

  def run(self):
    th_recv = threading.Thread(target=self.tc_recv.conduct, args=(self.running_recv, self.close_recv, ))
    th_recv.daemon = True
    th_recv.start()

    self.tc_trans.conduct(self.running_trans, self.close_trans)
    self.tc_recv.isConducting = False

    # try:
    #   while True:
    #     self.running()
    #     time.sleep(self.tc.sampling_time)
    # except KeyboardInterrupt:
    #   self.close()
    #   print('finish conduct')

if __name__ == "__main__":
  ui = UI(type='joystick controller')
  ui.run()
  print('finish safely')