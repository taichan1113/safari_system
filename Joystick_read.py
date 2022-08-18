import pygame
from pygame.locals import *
import time

# pygame初期化
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f'ジョイスティック名前: {joystick.get_name()}')
print(f'ボタン数: {joystick.get_numbuttons()}')
print(f'ジョイスティック軸数: {joystick.get_numaxes()}')


pygame.init()
now = time.time()
ts = 0.1
while True:
  try:
    if time.time() - now < ts:
      continue
    print('ジョイスティック:', [joystick.get_axis(0), -joystick.get_axis(5), -joystick.get_axis(4)])
    pygame.event.clear()
    now = time.time()
    # events = pygame.event.get()
    # for e in events:
    #   if e.type == QUIT:
    #     break
    #   if time.time() - now < ts:
    #     continue
    #   if e.type == pygame.locals.JOYAXISMOTION:
    #     print('ジョイスティック:', [joystick.get_axis(0), -joystick.get_axis(5), -joystick.get_axis(4)])
    #   elif e.type == pygame.locals.JOYBUTTONDOWN:
    #     print(f'ボタン{e.button}を押した')
    #   elif e.type == pygame.locals.JOYBUTTONUP:
    #     print(f'ボタン{e.button}を離した')
    #   now = time.time()

  except KeyboardInterrupt:
    break

