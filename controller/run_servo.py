import time
import RPi.GPIO as GPIO

SERVO_PIN = 17

class Servo:
  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_PIN, GPIO.OUT)
    self.pwm = GPIO.PWM(SERVO_PIN, 50)

  def init(self):
    self.pwm.start(0)
  
  def setAngle(self, angle):
    angle = max([angle, -90])
    angle = min([angle, 90])
    dc = 2.5 + (12.0-2.5)/180*(angle+90)
    
    self.pwm.ChangeDutyCycle(dc)
    time.sleep(0.1)
    self.pwm.ChangeDutyCycle(0.0)

if __name__ == "__main__":
  servo = Servo()
  servo.init()
  angle = 0
  incliment = 1
  while True:
    try:
      servo.setAngle(angle)
    except KeyboardInterrupt:
      break
    if angle >= 90:
      incliment = -1
    else:
      incliment = 1
    angle = angle + incliment
