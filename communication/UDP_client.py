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
  byteData = sock.recv(2**19)
  narray=numpy.fromstring(byteData, numpy.uint8)
  img_decode = cv2.imdecode(narray, cv2.IMREAD_COLOR)
  return img_decode

try:
  while True:
    img = getimage()
    # print(img)
    cv2.imshow('result', img)
    cv2.waitKey(1)
except KeyboardInterrupt:
  print('finished')