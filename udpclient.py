#!/usr/bin/env python3

# udpserver.pyで起動したlocalhost:9999に対しメッセージを送信する。
# 戻ってきたメッセージ(数字)を出力する。

import socket

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # sock.AF_INET: インターネット(IPv4)を使う
        # sock.SOCK_DGRAM: UDPを使う
sock.settimeout(1) # データが来ないとずっと待つのでタイムアウトを設定

# メッセージの送信
sock.sendto(b"Hello, World!", ('localhost', 9999))

# メッセージの受信
message, address = sock.recvfrom(8192)
print(f"Received {len(message)} bytes from {address}")
print(f"Message: {message.decode('utf-8')}")
sock.close()
