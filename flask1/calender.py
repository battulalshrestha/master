
'''from flask import Flask
from flask import url_for
app = Flask(__name__)
@app.route('/')
def index():
   return "index"
@app.route('/mobilenumber')
def profile(mobilenumber):
    return "mobilenumber"
@app.route('/passoword/<passwordpage>')
def profile(passwordpage):
   return f'{passwordpage}\'s profile'
while app.test_request_context():
   print(url_for("index"))
   print(url_for("mobilenumber"))
   print(url_for("profile",passwordpage ="nishan shrestha"))'''
from flask import Flask,url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
if __name__ == "__main__":
 app.run(debug= True)
                        

                           
