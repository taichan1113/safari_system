# -*- coding:utf-8 -*-
#!/usr/bin/python
import socket  
import numpy  
import cv2  
from dotenv import load_dotenv
import os

# load_dotenv('./.env')
# KB_RASPI_IP = os.getenv('KB_RASPI_IP')
def getimage():

    # 送信先のIPアドレスとポート番号を設定
    HOST = "127.0.0.1"
    # HOST = KB_RASPI_IP
    # HOST = "192.168.11.25"
    PORT = 8080
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
    sock.connect((HOST,PORT))   
    sock.send(b'test')

    # バイト型
    buf=b''   
    recvlen=100  
    while recvlen>0:  
        # receivedstr=sock.recv(1024)  
        receivedstr=sock.recv(1024*8)  
        recvlen=len(receivedstr)  
        buf += receivedstr
    sock.close()

    narray=numpy.fromstring(buf,dtype='uint8')
    return cv2.imdecode(narray,1)

while True:  
    img = getimage()
    cv2.imshow('Capture',img)  

    # qを入力すれば処理終了
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break