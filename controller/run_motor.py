import RPi.GPIO as GPIO
import sys
import time

class DCMotor():
    def __init__(self):
        self.PIN_IN1 = 13
        self.PIN_IN2 = 19
        self.freq = 10
        self.lowestDutyCycle = 20
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.PIN_IN1, GPIO.OUT)
        GPIO.setup(self.PIN_IN2, GPIO.OUT)
        self.pDrive = GPIO.PWM(self.PIN_IN1, self.freq)
        self.pBack = GPIO.PWM(self.PIN_IN2, self.freq)
        self.pDrive.start(0)
        self.pBack.start(0)
    
    def drive(self, dutyCycle):
        self.pDrive.ChangeDutyCycle(dutyCycle)
        self.pBack.ChangeDutyCycle(0)

    def back(self, dutyCycle):
        self.pDrive.ChangeDutyCycle(0)
        self.pBack.ChangeDutyCycle(dutyCycle)

    def stop(self):
        self.pDrive.ChangeDutyCycle(0)
        self.pBack.ChangeDutyCycle(0)
        
def test_function():
    motor = DCMotor()
    dc = 30
    try:
        print('system running')
        while True:
            #「e」キーが押されたら前進
            c = sys.stdin.read(1)
            if c == 'e':
                motor.drive(dc)
            #「d」キーが押されたら後退
            if c == 'd':
                motor.back(dc)
            #「q」キーが押されたら止まる
            if c == 'q':
                motor.stop()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    print('system running')
    motor = DCMotor()
    try:
        for i in range(5):
            dc = 20 + i*10
            motor.drive(dc)
            time.sleep(5)
        motor.stop()
    except KeyboardInterrupt:
        motor.stop()
        pass
        
    GPIO.cleanup()