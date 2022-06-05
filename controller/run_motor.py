import RPi.GPIO as GPIO
import sys
PIN_IN1 = 13
PIN_IN2 = 19
duty = 30 # >= 20%

#GPIO初期設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_IN1, GPIO.OUT)
GPIO.setup(PIN_IN2, GPIO.OUT)

p1 = GPIO.PWM(PIN_IN1, 10) #10Hz
p2 = GPIO.PWM(PIN_IN2, 10) #10Hz
            
p1.start(0)
p2.start(0)

try:
    print('system running')
    while True:
        #「e」キーが押されたら前進
        c = sys.stdin.read(1)
        if c == 'e':
            p1.ChangeDutyCycle(duty)
            p2.ChangeDutyCycle(0)
              
        #「d」キーが押されたら後退
        if c == 'd':
            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(duty)

        #「q」キーが押されたら止まる
        if c == 'q':
            p1.ChangeDutyCycle(0)
            p2.ChangeDutyCycle(0)

except KeyboardInterrupt:
    pass

GPIO.cleanup()