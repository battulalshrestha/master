from email import message
from flask import Flask,jsonify
'''app = Flask(__name__)
@app.route('/message')
def send_message():
   message = {" 'api_version' = '1.0','message' = 'hello nishan how you doing today:' "}
   return jsonify(message)
if __name__ == '__main__':
 app.run(debug= '404')  '''
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/message')
def get_message():
    message = {
        'api_version': '1.0',
        'message': 'Hello, World!'
    }
    return jsonify(message)

if __name__ == '__main__':
    app.run()
