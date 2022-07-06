# -*- coding:utf-8 -*-
# !/usr/bin/python

import socketserver
import cv2
import socket
import sys
import numpy
from dotenv import load_dotenv
import os

load_dotenv('./.env')
KB_RASPI_IP = os.getenv('KB_RASPI_IP')


class TCPHandler(socketserver.BaseRequestHandler):
    videoCap = cv2.VideoCapture(0)

    # リクエストを受け取るたびに呼ばれる関数
    def handle(self):
        # クライアントからデータを受け取ったらJPEG圧縮した映像を文字列にして送信
        self.data = self.request.recv(1024).strip()

        # readするたびにビデオのフレームを取得
        ret, frame = videoCap.read()

        # jpegの圧縮率を設定 0～100値が高いほど高品質。何も指定しなければ95
        # encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 100]

        # 文字列に変換
        jpegsByte = cv2.imencode('.jpeg', frame)[1].tostring()
        self.request.send(jpegsByte)


# このプログラムを起動している端末のIPアドレス
# HOST = "127.0.0.1"
HOST = KB_RASPI_IP
PORT = 8080

# ビデオの設定
videoCap = cv2.VideoCapture(0)

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