from socket import *
from contextlib import closing
import cv2
import time
import struct

## UDP送信クラス
class udptrans():
  def __init__(self, IP):
    DstIP = IP
    DstPort = 22222
    self.DstAddr = (DstIP, DstPort)

    self.udpClntSock = socket(AF_INET, SOCK_DGRAM)
    self.udpClntSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

  def transmit_characters(self, data):
    send_data = data.encode('utf-8')
    self.udpClntSock.sendto(send_data, self.DstAddr)

  def transmit_digits(self, data, format='>ddd'):
    send_data = struct.pack(format, data[0], data[1], data[2])
    # print("send: ", struct.unpack(format, send_data)) #送信したデータを送信側に表示
    self.udpClntSock.sendto(send_data, self.DstAddr)

  def transmit_img(self, frame, quality):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    encoded_image = cv2.imencode('.jpeg', frame, encode_param)[1]
    self.udpClntSock.sendto(encoded_image.tobytes(), self.DstAddr)

  def socketClose(self):
    self.udpClntSock.close()

def trans_digits_test():
  IP = "192.168.11.11"
  udp = udptrans(IP)
  with closing(udp.udpClntSock):
    data_el = 0
    while True:
      try:
        data = [data_el, data_el, data_el]
        udp.transmit_digits(data)
        data_el += 1
        time.sleep(0.1)
      except KeyboardInterrupt:
        udp.udpClntSock.close()
        break

def trans_img_test():
  IP = "192.168.11.11"
  # IP = "127.0.0.1"
  udp = udptrans(IP)
  with closing(udp.udpClntSock):
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920*0.6)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080*0.6)
    #capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
    t0 = time.time()
    try:
      while True:
        if time.time() - t0 < 0.03:
          continue
        ret, frame = capture.read()
        udp.transmit_img(frame, 30)
        t0 = time.time()
        # time.sleep(1)
    except KeyboardInterrupt:
      udp.udpClntSock.close()

if __name__ == '__main__':
  trans_img_test()
