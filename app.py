from flask import Flask
import threading
import os

def run():
	while True:
		print("runnning file")
		os.system(run.py)
x = threading.Thread(target=run)
x.start()
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'
