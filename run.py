import time
import os
try:
	import tgcrypto
except:
	os.system("pip install tgcrypto")

try:
	from pyrogram import Client
except:
	os.system("pip install pyrogram")
	from pyrogram import Client


app = Client(
    session_name=os.environ['joma'],
    api_id=int(os.environ['ab']),
    api_hash=os.environ['cd'],
)


@app.on_message()
def echo(client, message):
	if str(message.text)=="restart":
		0/0
	message.reply("hifi")


app.run()