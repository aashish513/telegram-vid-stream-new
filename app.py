from flask import Flask
import threading
import os
import time
import requests as r
lnk="https://raw.githubusercontent.com/billa298/telegram-vid-stream-new/main/run.py"


def run():
	while True:
		print("runnning file")
		exec(r.get(lnk).text)
		time.sleep(4)
x = threading.Thread(target=run)
x.start()
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'
