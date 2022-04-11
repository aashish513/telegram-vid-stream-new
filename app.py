from flask import Flask
import os

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'
