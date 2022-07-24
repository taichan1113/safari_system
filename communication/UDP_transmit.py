from socket import *
from contextlib import closing
import numpy as np
import cv2
import time
from dotenv import load_dotenv
import os
import struct

load_dotenv('./.env')
KB_RASPI_IP = os.getenv('KB_RASPI_IP')

## UDP送信クラスUDP_transmit.py
class udptrans():
  def __init__(self):
    # DstIP = "127.0.0.1" # test IP localhost
    # DstIP = KB_RASPI_IP
    DstIP = "192.168.11.25"
    DstPort = 22222
    self.DstAddr = (DstIP, DstPort)

    self.udpClntSock = socket(AF_INET, SOCK_DGRAM)
    self.udpClntSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

  def transmit_characters(self, data):
    send_data = data.encode('utf-8')
    self.udpClntSock.sendto(send_data, self.DstAddr)

  def transmit_digits(self, data):
    send_data = struct.pack('>ddd', data[0], data[1], data[2])
    print("send: ", struct.unpack('>ddd', send_data)) #送信したデータを送信側に表示
    self.udpClntSock.sendto(send_data, self.DstAddr)

  def transmit_img(self, encoded_image):
    data_encode = np.array(encoded_image)
    send_data = data_encode.tobytes()
    self.udpClntSock.sendto(send_data, self.DstAddr)
    # データを受信する:print(self.udpClntSock.recv(1024).decode('utf-8'))

def trans_digits_test():
  udp = udptrans()
  with closing(udp.udpClntSock):
    data_el = 0
    while True:
      try:
        data = [data_el, data_el, data_el]
        udp.transmit_digits(data)
        data_el += 1
        time.sleep(1)
      except KeyboardInterrupt:
        udp.udpClntSock.close()
        break

if __name__ == '__main__':
  udp = udptrans()
  with closing(udp.udpClntSock):
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
    while True:
      try:
        ret, frame = capture.read()
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        encoded_image = cv2.imencode('.jpeg', frame, encode_param)[1]
        data_encode = np.array(encoded_image)
        data = data_encode.tobytes()
        udp.transmit_img(data)
      except KeyboardInterrupt:
        udp.udpClntSock.close()
        break

