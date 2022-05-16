from socket import *
from contextlib import closing
import time
from dotenv import load_dotenv
import os

load_dotenv('./.env')
MY_RASPI_IP = os.getenv('MY_RASPI_IP')

## UDP送信クラス
class udptrans():
  def __init__(self):
    DstIP = MY_RASPI_IP # raspberry pi IP
    DstPort = 22222
    self.DstAddr = (DstIP, DstPort)

    self.udpClntSock = socket(AF_INET, SOCK_DGRAM)

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