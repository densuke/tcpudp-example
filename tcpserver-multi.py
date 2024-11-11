#!/usr/bin/env python3

# TCPを用いた簡易サーバー、9999を用いて待機し、クライアントからメッセージとして文字列を受け取る
# 受信したメッセージはそのままコンソールに表示する
# その後返信を行う、このとき返信されるデータはJSON形式で、以下の値を持つ。
# - original_message: 受信したメッセージ
# - message_length: 受信したメッセージの長さ
# - encoded_message: 受信したメッセージをBase64でエンコードしたもの
# - received_time: メッセージを受信した時刻(UNIX Epoch秒)
# ライブラリは標準で用意されいているもののみを使うこと。
# 今回はマルチスレッドで実装していること。

import socket
import json
import base64
import time
import threading

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9999))

def handle_client(connection, address):
    print(f"Connected by {address}")

    # メッセージの受信
    message = connection.recv(8192)
    print(f"Received {len(message)} bytes from {address}")
    print(f"Message: {message.decode('utf-8')}")

    # メッセージの返信
    response = {
        "original_message": message.decode('utf-8'),
        "message_length": len(message),
        "encoded_message": base64.b64encode(message).decode('utf-8'),
        "received_time": time.time()
    }
    connection.sendall(json.dumps(response).encode('utf-8'))

    # クライアントとの接続をクローズ
    connection.close()

while True:
    # クライアントからの接続を待機
    sock.listen(1)
    connection, address = sock.accept()
    client_thread = threading.Thread(target=handle_client, args=(connection, address))
    client_thread.start()
