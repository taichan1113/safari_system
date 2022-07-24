import csv
from mpu6050 import mpu6050

class DataLogger:
  def __init__(self):
    self.sensor = mpu6050(0x68)

  def log(self):
    try:
      with open('test.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["acc_x", "acc_y", "acc_z", "gyro_x", "gyro_y", "gyro_z"])
        print('file created')
        while True:
          accel_data = self.sensor.get_accel_data()
          gyro_data = self.sensor.get_gyro_data()
          data = [accel_data['x'], accel_data['y'], accel_data['z'], gyro_data['x'], gyro_data['y'], gyro_data['z'],]
          writer.writerow(data)
    except KeyboardInterrupt:
      print('file created')

if __name__ == "__main__":
    logger = DataLogger()
    logger.log()