#!/usr/bin/env python3

# udpserver.pyで起動したlocalhost:9999に対しメッセージを送信する。
# 戻ってきたメッセージ(数字)を出力する。

import socket

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# メッセージの送信
sock.sendto(b"Hello, World!", ('localhost', 9999))

# メッセージの受信
message, address = sock.recvfrom(8192)
print(f"Received {len(message)} bytes from {address}")
print(f"Message: {message.decode('utf-8')}")
sock.close()
