import pigpio
import time

PIN = 18

class Servo:
    def __init__(self):
        self.pi = pigpio.pi()
        self.pi.set_mode(PIN, pigpio.OUTPUT)
#         self.duty_ratio = 50 # [%]
        self.freq = int(50) # [Hz]
        
        
    def setAngle(self, angle, duration=0.5):
        angle = max([angle, -90])
        angle = min([angle, 90])
        dc = 2.5 + (12.0-2.5)/180*(angle+90) # duty cycle [%]
        
        duty = int(10000 * dc)
        self.pi.hardware_PWM(PIN, self.freq, duty) # Hz, duty

        time.sleep(duration)

if __name__ == "__main__":
    servo = Servo()
    angle = 0
    incliment = 10
    for i in range(100):
        print(angle)
        servo.setAngle(angle, duration=0.1)
        angle = (angle + incliment + 90)%180 - 90
    
    servo.setAngle(0)
    servo.pi.set_mode(PIN,pigpio.INPUT)
    servo.pi.stop()

