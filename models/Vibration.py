import numpy as np
import time

from sensor.mpu6050 import mpu6050

class Vibration:
  def __init__(self):
    self.sensor = mpu6050(0x68)
    self.N = 0

  def storeData(self):
    time_data = np.array([])
    count = 0
    return

  def FFT(self):
    # dt = 0.02
    # t = np.arange(0, N*dt, dt)
    # freq = np.linspace(0, 1.0/dt, N)

    while(True):
        for _ in range(N):
            ax = self.sensor.get_accel_data()['x']
            print(count)
            count += 1
            time_data = np.append(time_data, ax)
            time.sleep(0.02)
        
        #FFT
        F = np.fft.fft(time_data)
        Amp = np.abs(F)
        break