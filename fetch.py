#!/usr/bin/env python3
# 引数で渡されるURLのコンテンツを取得する
# 出力する際に、text系であればそのまま出すが、非text系の場合はContent-Typeを代わりに出して終了する
# ページ遷移が必要な場合は、リダイレクト先URLを出力して行うこととする

import sys
# requests: 非標準ライブラリです、pipで入れてください
import requests
import argparse

def fetch(url):

    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        if 400 <= r.status_code < 500:
            print(f"Client error: {r.status_code} - {http_err}", file=sys.stderr)
        elif 500 <= r.status_code < 600:
            print(f"Server error: {r.status_code} - {http_err}", file=sys.stderr)
        return
    except Exception as err:
        print(f"Other error occurred: {err}", file=sys.stderr)
        return
    if r.status_code == 200:
        if 'text' in r.headers['Content-Type']:
            print(r.text)

        else:
            print("Not text: " + r.headers['Content-Type'], file=sys.stderr)
    elif r.status_code in (301, 303):
        print(r.headers['Location'], file=sys.stderr)
    else:
        print(r.status_code)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='指定したURLの取得を試みます、テキストならそのまま出します')
    parser.add_argument('url', help='取得先URL')
    args = parser.parse_args()

    fetch(args.url)
