from socket import *
# from contextlib import closing
import struct
# from controller.run_servo_hardware import Servo

## UDP受信クラス
class udprecv():
  def __init__(self):
    SrcIP = ""
    SrcPort = 22222
    self.SrcAddr = (SrcIP, SrcPort)

    self.BUFSIZE = 1024
    self.udpServSock = socket(AF_INET, SOCK_DGRAM)
    self.udpServSock.bind(self.SrcAddr)

  def receive(self):
    try:
      data, addr = self.udpServSock.recvfrom(self.BUFSIZE)
    except KeyboardInterrupt:
      self.udpServSock.close()
    return data, addr

  def receive_characters(self):
    data, addr = self.receive()
    return data.decode()

  def receive_digits(self):
    data, addr = self.receive()
    return struct.unpack('>ddd' , data)

if __name__ == '__main__':
  udp = udprecv()
  # servo = Servo()

  try:
    while True:
      data, addr = udp.receive()
      digits = struct.unpack('>ddd' , data)
      print(digits[0])
      print(digits[1])
      # servo.setAngle(digits*-90, duration=0.1)
  except KeyboardInterrupt:
    udp.udpServSock.close()
