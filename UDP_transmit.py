from socket import *
from contextlib import closing
import time

## UDP送信クラス
class udptrans():
  def __init__(self):
    # SrcIP = "127.0.0.5"
    # SrcPort = 11111
    # self.SrcAddr = (SrcIP, SrcPort)

    DstIP = "127.0.0.1"
    DstPort = 22222
    self.DstAddr = (DstIP, DstPort)

    self.udpClntSock = socket(AF_INET, SOCK_DGRAM)
    # self.udpClntSock.bind(self.SrcAddr)

  def trsmt(self, data):
    send_data = data.encode('utf-8')
    self.udpClntSock.sendto(send_data, self.DstAddr)


if __name__ == '__main__':
  udp = udptrans()
  with closing(udp.udpClntSock):
    while True:
      try:
        udp.trsmt('test')
        time.sleep(1)
      except KeyboardInterrupt:
        udp.udpClntSock.close()
        break