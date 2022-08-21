from socket import *
import numpy as np
import struct
import cv2

## UDP受信クラス
class udprecv():
  def __init__(self, blocking=True):
    SrcIP = ""
    SrcPort = 22222
    self.SrcAddr = (SrcIP, SrcPort)

    self.BUFSIZE = 2**10
    self.udpServSock = socket(AF_INET, SOCK_DGRAM)
    self.udpServSock.bind(self.SrcAddr)
    self.udpServSock.setblocking(blocking)

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
    digits = struct.unpack('>ddd' , data)
    print(digits)
    return digits

  def receive_img(self):
    img_buffer = 2**19
    data, addr = self.udpServSock.recvfrom(img_buffer)
    np_arr = np.fromstring(data, np.uint8)
    img_decode = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img_decode

  def socketClose(self):
    self.udpServSock.close()

def recieve_digits_test():
  udp = udprecv()
  while True:
    try:
      data = udp.receive_digits()
      print(data)
    except Exception as e:
      print(e)
      break
  udp.udpServSock.close()

if __name__ == '__main__':
  udp = udprecv()
  while True:
    try:
      data = udp.receive_img()
      cv2.imshow('result', data)
      cv2.waitKey(int(30))
      # cv2.destroyAllWindows()
      
    except Exception as e:
      print(e)
      break
  udp.udpServSock.close()
