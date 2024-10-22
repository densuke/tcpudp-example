#!/usr/bin/env python3

# tcpserver.pyに対応するクライアントコード
# ランダムな名前(日本人名、UTF-8による漢字)を送信し、
# その処理結果を受け取る

import socket
import json
import base64
import time
import random
import os


# メッセージの作成
try:
    names_file_path = os.path.join(os.path.dirname(__file__), "names.txt")
    with open(names_file_path, "r") as file:
        names = file.readlines()
    if not names:
        raise ValueError("The names file is empty.")
    name = random.choice(names).strip()
except FileNotFoundError:
    print(f"Error: The file {names_file_path} was not found.")
    exit(1)
except ValueError as ve:
    print(f"Error: {ve}")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)

# ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #IPv4でストリームを作成 → これがTCPのこと(TCPソケット)
sock.connect(('localhost', 9999))

sock.sendall(name.encode('utf-8'))

# メッセージの受信
message = sock.recv(8192)
print(f"Received {len(message)} bytes")
print(f"Message: {message.decode('utf-8')}")
response = json.loads(message) # JSON形式を変換しておく
print(f"Original Message: {response['original_message']}")
print(f"Message Length: {response['message_length']}")
print(f"Encoded Message: {response['encoded_message']}")
print(f"Received Time: {response['received_time']}")
print("============================")
print(f"Decoded Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(response['received_time']))}")
print(f"Decoded Message: {base64.b64decode(response['encoded_message']).decode('utf-8')}")
sock.close()

