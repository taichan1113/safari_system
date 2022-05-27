import pygame
from pygame.locals import *
import time
from UDP_transmit import udptrans as Trans

# pygame初期化
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f'ジョイスティック名前: {joystick.get_name()}')
print(f'ボタン数: {joystick.get_numbuttons()}')
print(f'ジョイスティック軸数: {joystick.get_numaxes()}')


pygame.init()
trans = Trans()

while True:
  try:
    for e in pygame.event.get():
      if e.type == QUIT:
        break
      
      if e.type == pygame.locals.JOYAXISMOTION:
        print('ジョイスティック:', joystick.get_axis(0), joystick.get_axis(1), joystick.get_axis(2), joystick.get_axis(3))
        # trans.transmit_digits(joystick.get_axis(0))
      elif e.type == pygame.locals.JOYBUTTONDOWN:
        print(f'ボタン{e.button}を押した')
      elif e.type == pygame.locals.JOYBUTTONUP:
        print(f'ボタン{e.button}を離した')
  except KeyboardInterrupt:
    break

