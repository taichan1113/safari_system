import socket
import numpy
import cv2


def getimage():
  HOST, PORT = "localhost", 9999
  # SOCK_DGRAM is the socket type to use for UDP sockets
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  # As you can see, there is no connect() call; UDP has no connections.
  # Instead, data is directly sent to the recipient via sendto().
  sock.sendto(b'test', (HOST, PORT))

  # バイト型
  # buf=b''   
  # recvlen=100  
  # while recvlen>0:  
  #   # received = str(sock.recv(1024), "utf-8")
  #   # receivedstr=sock.recv(1024)  
  #   receivedstr=sock.recv(2**15)
  #   recvlen=len(receivedstr)  
  #   buf += receivedstr
  # sock.close()

  byteData = sock.recv(2**19)
  narray=numpy.fromstring(byteData, numpy.uint8)
  img_decode = cv2.imdecode(narray, cv2.IMREAD_COLOR)
  return img_decode

while True:
  try:
    img = getimage()
    # print(img)
    cv2.imshow('result', img)
    cv2.waitKey(1)
  except KeyboardInterrupt:
    print('finished')