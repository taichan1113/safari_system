from socket import *
from contextlib import closing
import struct
from controller.run_servo import Servo

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
    while True:
      data, addr = self.receive()
      print(data.decode(), addr)

  def receive_digits(self):
    while True:
      data, addr = self.receive()
      print(str( struct.unpack('>d' , data)[0] ), addr)


if __name__ == '__main__':
  udp = udprecv()
  # udp.receive_digits()
  servo = Servo()
  servo.init()
  while True:
    try:
      data, addr = udp.receive()
      digits = struct.unpack('>d' , data)[0]
      servo.setAngle(digits*90)
    except KeyboardInterrupt:
      break
