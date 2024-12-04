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

## ライブラリ
pip install pytz discord ping3 requests cloudflare_ddns
