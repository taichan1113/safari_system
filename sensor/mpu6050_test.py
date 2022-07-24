import smbus
import time

#I2C設定
i2c = smbus.SMBus(1)
dev_addr = 0x68

#MPU-6050設定
#CONFIGレジスタ
i2c.write_byte_data(dev_addr, 0x1a, 0x00)

#GYRO_CONFIGレジスタ
i2c.write_byte_data(dev_addr, 0x1b, 0x00)

#ACCEL_CONFIGレジスタ
i2c.write_byte_data(dev_addr, 0x1c, 0x00)

#PWR_MGMT_1レジスタ
i2c.write_byte_data(dev_addr, 0x6b, 0x00)

#繰り返し
while True:

    #加速度データ読み込み
    acc_x = i2c.read_word_data(dev_addr, 0x3b)
    acc_y = i2c.read_word_data(dev_addr, 0x3d)
    acc_z = i2c.read_word_data(dev_addr, 0x3f)
        
    #角速度データ読み込み
    gyr_x = i2c.read_word_data(dev_addr, 0x43)
    gyr_y = i2c.read_word_data(dev_addr, 0x45)
    gyr_z = i2c.read_word_data(dev_addr, 0x47)
    
    #温度データ読み込み
    tmp = i2c.read_word_data(dev_addr, 0x41)
    
    #加速度データ変換
    acc_x = (acc_x << 8) & 0xFF00 | (acc_x >> 8)
    acc_y = (acc_y << 8) & 0xFF00 | (acc_y >> 8)
    acc_z = (acc_z << 8) & 0xFF00 | (acc_z >> 8)
    
    #角速度データ変換
    gyr_x = (gyr_x << 8) & 0xFF00 | (gyr_x >> 8)
    gyr_y = (gyr_y << 8) & 0xFF00 | (gyr_y >> 8)
    gyr_z = (gyr_z << 8) & 0xFF00 | (gyr_z >> 8)
    
    #温度データ変換
    tmp = (tmp << 8) & 0xFF00 | (tmp >> 8)
    
    #加速度極性判断
    if acc_x >= 32768:
        acc_x -= 65536
    
    if acc_y >= 32768:
        acc_y -= 65536
    
    if acc_z >= 32768:
        acc_z -= 65536
    
    #角速度極性判断
    if gyr_x >= 32768:
        gyr_x -= 65536
    
    if gyr_y >= 32768:
        gyr_y -= 65536
    
    if gyr_z >= 32768:
        gyr_z -= 65536
    
    #温度極性判断
    if tmp >= 32768:
        tmp -= 65536
    
    #加速度を物理量に変換
    acc_x = acc_x / 16384.0
    acc_y = acc_y / 16384.0
    acc_z = acc_z / 16384.0
    
    #角速度を物理量に変換
    gyr_x = gyr_x / 131.0
    gyr_y = gyr_y / 131.0
    gyr_z = gyr_z / 131.0
    
    #温度を物理量に変換
    tmp = tmp / 340 + 36.53
    
    #加速度表示
    print('acc x:' + str(acc_x))
    print('acc y:' + str(acc_y))
    print('acc z:' + str(acc_z))
    
    #角速度表示
    print('gyr x:' + str(gyr_x))
    print('gyr y:' + str(gyr_y))
    print('gyr z:' + str(gyr_z))
    
    #温度表示
    print('tmp:' + str(tmp))
    
    time.sleep(0.5)