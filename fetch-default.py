#!/usr/bin/env python3
# Pythonの標準ライブラリの範囲のみで、指定URLの内容を取得します。
# 引数からURLを受け取り、その内容を表示します。

# 引数からURLを取得する
import sys
import urllib.request
import argparse

def fetch(url):
    try:
        with urllib.request.urlopen(url) as res:
            if 'text' in res.headers['Content-Type']:
                print(res.read().decode('utf-8'))
            else:
                print("Not text: " + res.headers['Content-Type'], file=sys.stderr)
    except urllib.error.URLError as e:
        print(f"Failed to fetch {url}: {e.reason}", file=sys.stderr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='指定したURLの取得を試みます、テキストならそのまま出します')
    parser.add_argument('url', help='取得先URL')
    args = parser.parse_args()

    fetch(args.url)
