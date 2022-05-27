from socket import *
from contextlib import closing
import struct
import time
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

  def recieve(self):
    try:
      data, addr = self.udpServSock.recvfrom(self.BUFSIZE)
    except KeyboardInterrupt:
      self.udpServSock.close()
    return data, addr
  
  def receive_handler(self, callback):
    data, addr = self.recieve()
    callback(data)

  def recieve_characters(self):
    while True:
      data, addr = self.recieve()
      print(data.decode(), addr)

  def recieve_digits(self):
    while True:
      data, addr = self.recieve()
      print(str( struct.unpack('>d' , data)[0] ) , addr)

if __name__ == '__main__':
    udp = udprecv()
    servo = Servo()
    servo.init()
    # udp.recieve_digits()
    while True:
      data, addr = udp.recieve()
      digits = struct.unpack('>d' , data)[0]
      servo.setAngle(digits*90)
      print(f'{digits*90.0} [deg]')
      # time.sleep(0.5)

