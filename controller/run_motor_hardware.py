import pigpio
import sys

PIN_IN1 = 13
PIN_IN2 = 19

p1 = pigpio.pi()
p2 = pigpio.pi()

p1.set_mode(PIN_IN1, pigpio.OUTPUT)
p2.set_mode(PIN_IN2, pigpio.OUTPUT)

freq = int(50) # [Hz]
dc = 80 # [%]
duty = int(10000 * dc)

try:
    print('system running')
    while True:
        #「e」キーが押されたら前進
        c = sys.stdin.read(1)
        if c == 'e':
            p1.hardware_PWM(PIN_IN1, freq, duty)
            p2.hardware_PWM(PIN_IN2, freq, 0)
              
        #「d」キーが押されたら後退
        if c == 'd':
            p1.hardware_PWM(PIN_IN1, freq, 0)
            p2.hardware_PWM(PIN_IN2, freq, duty)

        #「q」キーが押されたら止まる
        if c == 'q':
            p1.hardware_PWM(PIN_IN1, freq, 0)
            p2.hardware_PWM(PIN_IN2, freq, 0)

except KeyboardInterrupt:
    pass

p1.set_mode(PIN_IN1, pigpio.INPUT)
p2.set_mode(PIN_IN2, pigpio.INPUT)
p1.stop()
p2.stop()
