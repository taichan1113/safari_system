import pygame
from pygame.locals import *
from communication.UDP_transmit import udptrans as Trans
import time

# pygame初期化
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f'ジョイスティック名前: {joystick.get_name()}')
print(f'ボタン数: {joystick.get_numbuttons()}')
print(f'ジョイスティック軸数: {joystick.get_numaxes()}')


pygame.init()
trans = Trans()
now = time.time()

while True:
  try:
    for e in pygame.event.get():
      if e.type == QUIT:
        break
      if time.time() - now < 0.1:
        continue
      
      if e.type == pygame.locals.JOYAXISMOTION:
        # print('ジョイスティック:', joystick.get_axis(0), joystick.get_axis(1), joystick.get_axis(2), joystick.get_axis(3))
        print([joystick.get_axis(0), joystick.get_axis(1)])
        # trans.transmit_digits(joystick.get_axis(0))
      elif e.type == pygame.locals.JOYBUTTONDOWN:
        print(f'ボタン{e.button}を押した')
      elif e.type == pygame.locals.JOYBUTTONUP:
        print(f'ボタン{e.button}を離した')
      now = time.time()

  except KeyboardInterrupt:
    break

