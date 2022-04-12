print("restarted")

import os


try:
	from pyrogram import Client
except:
	os.system("pip install pyrogram")
	from pyrogram import Client


app = Client(
    session_name='hi',
    api_id=int(os.environ['ab']),
    api_hash=os.environ['cd'],
)
with app:
    print(app.export_session_string())




