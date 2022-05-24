import serial

comport = serial.Serial('COM4', baudrate=19200, parity=serial.PARITY_NONE)
recv_data = comport.read(12)
meas_data = float(recv_data.decode('utf-8').split('+')[1])
comport.close()

# ports = ['COM%s' % (i + 1) for i in range(256)]
# for port in ports:
#   try:
#     s = serial.Serial(port)
#     s.close()
#     print(port)
#   except (OSError, serial.SerialException):
#     pass
