# ソケットライブラリ取り込み
import socket

# サーバーIPとポート番号
# IPADDR = "127.0.0.1"
IPADDR = "192.168.11.2"
PORT = 49152

# ソケット作成
sock = socket.socket(socket.AF_INET)
# サーバーへ接続
sock.connect((IPADDR, PORT))

# byte 形式でデータ送信
sock.send("hello".encode("utf-8"))

# 送信無限ループ
while True:
    # 任意の文字を入力
    data = input("> ")
    # サーバーに送信
    sock.send(data.encode("utf-8"))