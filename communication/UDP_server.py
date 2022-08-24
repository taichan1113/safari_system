import socketserver
import cv2

class MyUDPHandler(socketserver.BaseRequestHandler):
    capture = ''

    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print(data)

        # readするたびにビデオのフレームを取得
        ret, frame = capture.read()

        # jpegの圧縮率を設定 0～100値が高いほど高品質。何も指定しなければ95
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 30]

        # 文字列に変換
        jpegsByte = cv2.imencode('.jpeg', frame, encode_param)[1].tobytes()
        socket.sendto(jpegsByte, self.client_address)

if __name__ == "__main__":
    HOST, PORT = "192.168.11.16", 9999
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920*0.6)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080*0.6)
    capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))
    with socketserver.UDPServer((HOST, PORT), MyUDPHandler) as server:
        server.serve_forever()