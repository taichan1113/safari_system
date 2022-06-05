import pigpio
import time
import numpy as np

PIN = 18

class Servo:
    def __init__(self):
        self.pi = pigpio.pi()
        self.pi.set_mode(PIN, pigpio.OUTPUT)
#         self.duty_ratio = 50 # [%]
        self.freq = int(50) # [Hz]
        
        
    def setAngle(self, angle, duration=0.01):
        angle = max([angle, -90])
        angle = min([angle, 90])
        dc = 2.5 + (12.0-2.5)/180*(angle+90) # duty cycle [%]
        
        duty = int(10000 * dc)
        self.pi.hardware_PWM(PIN, self.freq, duty) # Hz, duty

        time.sleep(duration)

if __name__ == "__main__":
    print('start')
    servo = Servo()
    T = 2
    w = 2*np.pi/T
    t0 = time.time()
    try:
        while True:
            t = time.time() - t0
            angle = 90 * np.sin(w*t)
            servo.setAngle(angle, duration=0)
#             time.sleep(0.01)
    except KeyboardInterrupt:
        servo.setAngle(0, duration = 0.5)
        servo.pi.set_mode(PIN,pigpio.INPUT)
        servo.pi.stop()

