# 概要
SONY RC-S380を利用して東京理科大学学生証から学籍番号を抜き出して部室の入退室をdiscordに通知するツールです  
学籍番号とdiscord idの照合や入退室状況の保存のとえバックエンドとしてAWSを利用しています  

TODO:Cloudformation fileを乗せる

# 動かし方
`python 3.10`で動作確認済み
## 初期セットアップ
### カードリーダー関係
usbを認識するための設定を行います
```
./make-env.sh
```
終了後再起動してください（必要ないかも）
### python関係 
```
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
```
### 自動起動(*ローカル実行確認後に行う)
```
./register-service.sh
```
## ローカル実行
```
python3 main.py
```
