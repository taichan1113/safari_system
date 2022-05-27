from socket import *
from contextlib import closing
import time
from dotenv import load_dotenv
import os
import struct

load_dotenv('./.env')
MY_RASPI_IP = os.getenv('MY_RASPI_IP')

## UDP送信クラスUDP_transmit.py
class udptrans():
  def __init__(self):
    DstIP = "127.0.0.1" # test IP localhost
    # DstIP = MY_RASPI_IP
    DstPort = 22222
    self.DstAddr = (DstIP, DstPort)

    self.udpClntSock = socket(AF_INET, SOCK_DGRAM)
    self.udpClntSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

  def transmit_characters(self, data):
    send_data = data.encode('utf-8')
    self.udpClntSock.sendto(send_data, self.DstAddr)

  def transmit_digits(self, data):
    send_data = struct.pack('>d', data)
    print("send: ", send_data) #送信したバイト列を送信側に表示
    self.udpClntSock.sendto(send_data, self.DstAddr)


if __name__ == '__main__':
  udp = udptrans()
  with closing(udp.udpClntSock):
    data = 0
    while True:
      try:
        udp.transmit_digits(data)
        data += 1
        time.sleep(1)
      except KeyboardInterrupt:
        udp.udpClntSock.close()
        break