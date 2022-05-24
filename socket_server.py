# ソケットライブラリ取り込み
import socket

# サーバーIPとポート番号
# IPADDR = "127.0.0.1"
IPADDR = "192.168.11.2"
PORT = 49152

# AF_INET：IPv4形式でソケット作成(省略可)
sock_sv = socket.socket(socket.AF_INET)
# IPアドレスとポート番号でバインド、タプルで指定
sock_sv.bind((IPADDR, PORT))
# サーバー有効化
sock_sv.listen()

# クライアントの接続受付
sock_cl, addr = sock_sv.accept()

# 接続・受信の無限ループ
while True:
    # ソケットから byte 形式でデータ受信
    data = sock_cl.recv(1024)
    print(data.decode("utf-8"))
    # クライアントのソケットを閉じる
    # sock_cl.close()