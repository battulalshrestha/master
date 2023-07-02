from flask import Flask,jsonify
app = Flask(__name__)
@app.route('/')
def home():
   return "HELLO THIS IS MY WEB PAGE<h1>my name is nishan shrestha<h1> <h2> i live in rautepani <h2> <h3> i am recently studying elctronic and communication engineering now<h3>"
if __name__ == "__main__":
  app.run(debug = True)