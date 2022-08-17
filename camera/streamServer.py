# -*- coding:utf-8 -*-
# !/usr/bin/python

import socketserver
import cv2
import socket
import sys
import numpy
# from dotenv import load_dotenv
# import os

# load_dotenv('./.env')
# IP = os.getenv('MY_RASPIZERO2_IP')

class TCPHandler(socketserver.BaseRequestHandler):
    videoCap = ''

    # リクエストを受け取るたびに呼ばれる関数
    def handle(self):
        # クライアントからデータを受け取ったらJPEG圧縮した映像を文字列にして送信
        self.data = self.request.recv(1024).strip()
        # self.data = self.request[0].strip()
        # self.socket = self.request[1]

        # readするたびにビデオのフレームを取得
        ret, frame = videoCap.read()

        # jpegの圧縮率を設定 0～100値が高いほど高品質。何も指定しなければ95
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 95]

        # 文字列に変換
        jpegsByte = cv2.imencode('.jpeg', frame, encode_param)[1].tobytes()
        self.request.send(jpegsByte)
        # self.socket.sendto(jpegsByte, self.client_address)


# このプログラムを起動している端末のIPアドレス
HOST = "127.0.0.1"
# HOST = IP
PORT = 8080

# ビデオの設定
videoCap = cv2.VideoCapture(0)
# videoCap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# videoCap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# videoCap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('H', '2', '6', '4'))

if not videoCap:
    print ("ビデオが開けませんでした。")
    sys.exit()

socketserver.TCPServer.allow_reuse_address = True
server = socketserver.TCPServer((HOST, PORT), TCPHandler)

try:
    server.serve_forever()
except KeyboardInterrupt:
    pass
server.shutdown()
sys.exit()