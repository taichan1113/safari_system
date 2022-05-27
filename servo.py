import time

#GPIOの初期設定
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

SERVO_PIN = 17

#GPIO出力端子設定
GPIO.setup(SERVO_PIN, GPIO.OUT)

#GPIOPWM設定、周波数は50Hz
p = GPIO.PWM(SERVO_PIN, 50)

#Duty Cycle 0%
p.start(0.0)

while True:
    print("input angle degree (-90 - 90)")
    angle = float(input())
    angle = max([angle, -90])
    angle = min([angle, 90])
    dc = 2.5 + (12.0-2.5)/180*(angle+90)
#     dc = float(input())

    #DutyCycle dc%
    p.ChangeDutyCycle(dc)

    #最大180°回転を想定し、0.3sec以上待つ
    time.sleep(0.5)

    #回転終了したら一旦DutyCycle0%にする
    p.ChangeDutyCycle(0.0)