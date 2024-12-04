# DiscordBot
自宅サーバーを監視するシンプルなDiscordのBot。まだ制作初期段階なのでガバい。  
正直なところめちゃくちゃ個人用。

## 機能
!**** でコマンドを実行。
* サーバーのGlobal IPアドレスを取得
* !status コマンドでどのマシンからPingがこないかをチェック

## Background Task
デフォルトだと5分に1回実行されるタスクです。
* CloudFlareにIPアドレスを通知する
* 各VM/マシンにPingを飛ばして生きてるかを確認、それに応じてBOTのステータスを変更

## ToDo
* 全体的な信頼性の向上
* サーバーのハードウェア的な障害の検出
* HTTPリクエスト等の、Ping以外の信頼性の高いチェックメソッドを追加

## 実行
pip install pytz discord ping3 requests cloudflare_ddns
python3 main.py
