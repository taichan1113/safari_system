import time
import datetime
import csv
from sensor.mpu6050 import mpu6050

class DataLogger:
  def __init__(self):
    self.sensor = mpu6050(0x69)
    self.sampling_time = 0.1
    self.now = None

  def log(self):
    try:
      date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

      with open('{date}.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["time", "acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z"])
        print('file opened')
        self.now = time.time()
        t = 0
        while True:
          if time.time() - self.now < self.sampling_time:
            continue
          accel_data = self.sensor.get_accel_data()
          gyro_data = self.sensor.get_gyro_data()
          data = [t, accel_data['x'], accel_data['y'], accel_data['z'], gyro_data['x'], gyro_data['y'], gyro_data['z'],]
          writer.writerow(data)
          
          t += time.time() - self.now
          self.now = time.time()
    except KeyboardInterrupt:
      print('file created')

if __name__ == "__main__":
    logger = DataLogger()
    logger.log()