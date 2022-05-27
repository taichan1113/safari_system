import pygame
from pygame.locals import *
import time

# pygame初期化
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f'ジョイスティック名前: {joystick.get_name()}')
print(f'ボタン数: {joystick.get_numbuttons()}')


pygame.init()


while True:
  try:
    for e in pygame.event.get():
      if e.type == QUIT:
        break
      
      if e.type == pygame.locals.JOYAXISMOTION:
        print('十字キー:', joystick.get_axis(0), joystick.get_axis(1))
      elif e.type == pygame.locals.JOYBUTTONDOWN:
        print(f'ボタン{e.button}を押した')
      elif e.type == pygame.locals.JOYBUTTONUP:
        print(f'ボタン{e.button}を離した')
  except KeyboardInterrupt:
    break

