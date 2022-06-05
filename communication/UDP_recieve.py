from socket import *
# from contextlib import closing
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

  def receive(self):
    try:
      data, addr = self.udpServSock.recvfrom(self.BUFSIZE)
      return data, addr
    except Exception as e:
      print(e)
      pass
    
  def receive_characters(self):
    data, addr = self.receive()
    return data.decode()

  def receive_digits(self):
    data, addr = self.receive()
    return struct.unpack('>ddd' , data)

if __name__ == '__main__':
  udp = udprecv()
  while True:
    try:
      data = udp.receive_digits()
      print(data)
    except Exception as e:
      print(e)
      break
  udp.udpServSock.close()
