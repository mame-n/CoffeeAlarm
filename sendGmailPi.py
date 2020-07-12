#!/usr/bin python3
# -*- coding: utf-8 -*-

"""
	ラズパイ(Raspberry Pi)でGmail送信をやってみる
		python 3.2.5
		OS: Rasbian(Raspberry Pi Model B)
"""

# メール送信のためのSMTPセッションクライアントを作成するため
import smtplib

# メールの送信日付をインターネットで送信できるフォーマットで指定するため
from email.utils import formatdate

# メール本文に日本語を送信できるようにするためのMIME規格に変換するため（E-mailも基本は英語圏でできた規格なのです！）
from email.mime.text import MIMEText

if __name__ == "__main__":

	# Gmailアカウント設定
	gmail_addr = "coffeecom.ulkai@gmail.com"		# 例）hogehoge@gmail.com
	gmail_pass = "ContaxT2"	# 例）abc123xyz
	SMTP = "smtp.gmail.com"
	PORT = 587
		
	# 送信メール情報
	from_addr = gmail_addr				# 送信元メールアドレス（Gmailでなくてもよい）
	to_addr = "trigger@applet.ifttt.com"		# 例）helloworld@yahoo.com
	subject = "12:34 #CoffeeComplete"		# 件名
	body = ""	# 本文
	# メールメッセージを作成
	msg = MIMEText(body, "plain", "utf-8")	# ラズパイのpython3では3つの引数でエンコードをutf-8にしないと
						# 'ascii' codec can't encode characters in position 0-14: ordinal not in range(128) というエラーがでる
	msg["From"] = from_addr
	msg["To"] = to_addr
	msg["Date"] = formatdate()			# 日付をインターネットで送信できるフォーマットで指定
	msg["Subject"] = subject
		
	# メール送信
	try:
		print("メール送信中...")
		send = smtplib.SMTP(SMTP, PORT)		# GmailのSMTPを利用してSMTPオブジェクトを生成
		send.ehlo()
		send.starttls()
		send.ehlo()
		send.login(gmail_addr, gmail_pass)	# Gmailにログイン
		send.send_message(msg)			# メールを送信
		send.close()
	except Exception as e:
		print("except: " + str(e))		# エラー送出時のメッセージ表示
	else:
		print("{0}へメール送信したよ！".format(to_addr))	# メールが正常に送信されたときのメッセージ
