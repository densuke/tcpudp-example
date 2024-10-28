#!/usr/bin/env python3

# Flaskを使った簡易アプリケーションサーバーの例

from flask import Flask, request
import sys
import logging

app = Flask(__name__)

# ログの設定、INFO以上のログをコンソールに出す設定
log = logging.getLogger('app')
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler(sys.stdout))

@app.route('/')
def index():
    return 'Hello, World!'

# /echoにPOSTで文字列を送ると、逆さまにした文字列(+改行コード)を返す
@app.route('/echo', methods=['POST'])
def echo():
    # POSTで受け取ったデータを取得する
    data = request.get_data(as_text=True)
    log.info(f"input: '{data}'")
    # 逆さまにして返す
    return data[::-1] + '\n'

if __name__ == '__main__':
    app.run()

