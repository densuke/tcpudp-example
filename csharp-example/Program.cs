/** localhostの9999/tcpに接続し、適当な名前を送信して、戻りデータをダンプする

- 送信データ
    - ../names.txtに含まれている名前からランダムに1つ選び、送信する
- 受信データ
    - JSON形式のデータで届き、以下のようなデータが含まれている
        - original_message: 送信した名前
        - message_length: 送信した名前の長さ
        - encoded_message: base64エンコードした名前
        - received_time: 受信した時間(ナノ秒を含む)
*/

using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Text.Json;

class Program   {
    static void Main() {
        // 送信データの準備
        string[] names = File.ReadAllLines("../names.txt");
        string name = names[new Random().Next(names.Length)];

        // 送信データのダンプ
        Console.WriteLine($"Send: {name}");

        // 送信データのエンコード
        byte[] sendBytes = Encoding.UTF8.GetBytes(name);

        // ソケットの生成
        using (var client = new TcpClient("localhost", 9999)) {
            // ネットワークストリームの取得
            using (var stream = client.GetStream()) {
                // 送信
                stream.Write(sendBytes, 0, sendBytes.Length);

                // 受信
                byte[] receiveBytes = new byte[1024];
                int byteSize = stream.Read(receiveBytes, 0, receiveBytes.Length);
                string receiveData = Encoding.UTF8.GetString(receiveBytes, 0, byteSize);

                // 受信データのダンプ
                Console.WriteLine($"Receive: {receiveData}");

                // JSONデータのパース
                var json = JsonDocument.Parse(receiveData).RootElement;
                Console.WriteLine($"original_message: {json.GetProperty("original_message").GetString()}");
                Console.WriteLine($"message_length: {json.GetProperty("message_length").GetInt32()}");
                Console.WriteLine($"encoded_message: {json.GetProperty("encoded_message").GetString()}");
                // received_timeは小数を含む数値のため、GetString()ではなくGetDouble()を使用
                var rt = json.GetProperty("received_time").GetDouble();
                // rtはいわゆるEpoch秒なので、変換してISOの日時の文字列にする
                Console.WriteLine($"received_time: {DateTimeOffset.FromUnixTimeSeconds((long)rt).ToString("yyyy-MM-dd HH:mm:ss.ffffff")}");
            }
        }
    }
}

