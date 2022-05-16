from socket import *

## UDP受信クラス
class udprecv():
  def __init__(self):

    SrcIP = "127.0.0.1"
    SrcPort = 22222
    self.SrcAddr = (SrcIP, SrcPort)

    self.BUFSIZE = 1024
    self.udpServSock = socket(AF_INET, SOCK_DGRAM)
    self.udpServSock.bind(self.SrcAddr)

  def recv(self):
    while True:
      try:
        data, addr = self.udpServSock.recvfrom(self.BUFSIZE)
        print(data.decode(), addr)
      except KeyboardInterrupt:
        self.udpServSock.close()
        break

if __name__ == '__main__':
    udp = udprecv()     # クラス呼び出し
    udp.recv()          # 関数実行