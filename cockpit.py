import pygame
from pygame.locals import *
from communication import UDP_recieve, UDP_transmit
import cv2
import time
from dotenv import load_dotenv
import os
# import threading

load_dotenv('./.env')
IP = os.getenv('MY_RASPIZERO2_IP')

class UI:
  def __init__(self, type='handle controller'):
    self.isRunning = False
    # pygame初期化
    pygame.init()
    self.joystick = pygame.joystick.Joystick(0)
    self.joystick.init()
    print(f'ジョイスティック名前: {self.joystick.get_name()}')
    print(f'ボタン数: {self.joystick.get_numbuttons()}')
    print(f'ジョイスティック軸数: {self.joystick.get_numaxes()}')
    # 通信手段
    self.trans = UDP_transmit.udptrans(IP)
    self.recv = UDP_recieve.udprecv()
    # 時間制御
    self.rap_time = 0.05
    self.now = None
    # コントローラータイプ
    self.type = type

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

  def showCapture(self):
    img = self.recv.receive_img()
    cv2.imshow('result', img)
    cv2.waitKey(int(self.rap_time*1000)) # sec to msec

  def run(self):
    self.now = time.time()
    while self.isRunning:
      try:
        for e in pygame.event.get():
          if e.type == QUIT:
            break
          # self.printSignal(e)
          if time.time() - self.now < self.rap_time:
            continue
          self.transmitSignal(e)
          self.showCapture()

          # update time
          self.now = time.time()

      except KeyboardInterrupt:
        self.isRunning = False
        cv2.destroyAllWindows()
        self.recv.udpServSock.close()
        self.trans.udpClntSock.close()
        print('stop run')
        break
    
if __name__ == "__main__":
  ui = UI(type='joystick controller')
  ui.run()
  print('finish safely')