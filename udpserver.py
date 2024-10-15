#!/usr/bin/env python3
# UDPを用いた簡易サーバー、9999を用いて待機し、
# 受信したメッセージをコンソースに表示しつつ、その文字数を返信する
# ライブラリは標準で用意されいているもののみを使うこと。

import socket

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 9999))

while True:
    # メッセージの受信
    message, address = sock.recvfrom(8192)
    print(f"Received {len(message)} bytes from {address}")
    print(f"Message: {message.decode('utf-8')}")

    # メッセージの長さを返信
    sock.sendto(str(len(message)).encode('utf-8'), address)

# ソケットのクローズ
sock.close()
