from flask import Flask, send_from_directory
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/run.py')
def down():
  response = send_from_directory('/home/runner/telegram-vid-stream-new','run.py')
  return response


	

app.run(host='0.0.0.0', port=8080)
