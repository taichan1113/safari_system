import time
import datetime
import csv
from sensor.mpu6050 import mpu6050

class DataLogger():
  def __init__(self, sampling_time=0.05):
    self.sensor = mpu6050(0x69)
    self.sampling_time = sampling_time
    self.now = None
    self.isLogging = False

  def log(self):
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    with open(date+'.csv', 'a', newline='') as f:
      writer = csv.writer(f)
      writer.writerow(["time", "acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z"])
      print('logging started')
      self.now = time.time()
      t = 0
      while self.isLogging:
        if time.time() - self.now < self.sampling_time:
          continue
        t += time.time() - self.now
        self.now = time.time()
        try:
          accel_data = self.sensor.get_accel_data()
          gyro_data = self.sensor.get_gyro_data()
          data = [t, accel_data['x'], accel_data['y'], accel_data['z'], gyro_data['x'], gyro_data['y'], gyro_data['z'],]
          writer.writerow(data)
        except:
          print('logging error')

      print('logging finished')

if __name__ == "__main__":
    logger = DataLogger()
    logger.log()