import imp
from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/')
def helloworld():
  return "Nishan page"
if __name__ == '__main__':
  app.run(debug = True)
