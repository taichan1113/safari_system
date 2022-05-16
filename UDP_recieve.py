from socket import *
from contextlib import closing
import struct

## UDP受信クラス
class udprecv():
  def __init__(self):
    SrcIP = ""
    SrcPort = 22222
    self.SrcAddr = (SrcIP, SrcPort)

    self.BUFSIZE = 1024
    self.udpServSock = socket(AF_INET, SOCK_DGRAM)
    self.udpServSock.bind(self.SrcAddr)

  def recieve_characters(self):
    with closing(self.udpServSock):
      while True:
        try:
          data, addr = self.udpServSock.recvfrom(self.BUFSIZE)
          print(data.decode(), addr)
        except KeyboardInterrupt:
          self.udpServSock.close()
          break

  def recieve_digits(self):
    with closing(self.udpServSock):
      while True:
        try:
          data, addr = self.udpServSock.recvfrom(self.BUFSIZE)
          print(str( struct.unpack('>d' , data)[0] ) , addr)
        except KeyboardInterrupt:
          self.udpServSock.close()
          break

if __name__ == '__main__':
    udp = udprecv()
    udp.recieve_digits()