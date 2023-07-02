'''
from flask import Flask, jsonify, request, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fbe8a0cacc884a498e915dc44d86c782'

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert': "Token is missing"}), 401
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])
        except jwt.ExpiredSignatureError:
            return jsonify({'Alert': "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({'Alert': "Invalid token"}), 401
        return func(*args, **kwargs)

    return decorated

@app.route('/')
def page():
    if not session.get('logged_in'):
        return render_template("logged_in.html")
    else:
        return "Opened it currently"

@app.route('/public')
def public():
    return 'For public'

@app.route('/auth')
@token_required
def auth():
    return "JWT is verified. Welcome to your dashboard"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password == '123456':
        session['logged_in'] = True
        token = jwt.encode({
            'user': username,
            'expiration': datetime.utcnow() + timedelta(seconds=120)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token.decode("utf-8")})
    else:
        return make_response("Unable to verify", 403, {'WWW-Authenticate': 'Basic realm="Authentication Failed!"'})

if __name__ == '__main__':
    app.run(debug=True)'''
from ctypes import addressof
from operator import truediv
from secrets import token_bytes, token_urlsafe
from urllib.parse import scheme_chars
from flask import Flask, jsonify, request, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

from program2 import page, token_required
app = Flask(__name__)
app.config['python-key'] = "4988ede1-1590-4388-ab25-0f91cc8d8213"
def enter_mobile(func):
       @wraps(func)
       def enter_app(*args, **kwargs):
        page = request.args.get('page')
        if not page:
            return jsonify({'Alert': "page is missing"}), 402
        try: 
              second_opage = jwt.decode(page, app.config[''])
        except jwt.ExpiredSignatureError:
            return jsonify({'Alert': "page has expired"}), 402
        except jwt.InvalidTokenError:
            return jsonify({'Alert': "Invalid page"}), 402
        return func(*args, **kwargs)

       return enter_mobile

@app.route('/')
def sub_page():
    if not session.get('entered_in'):
        return render_template("entered_in.html")
    else:
        return "Opened it currently"

@app.route('/public')
def general():
    return 'For all'# lets see

@app.route('/self')
@token_required
def path():
    return "JWT is verified. Welcome .you can see your window"

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    email ="nishanshrestha2059@gmail.com" 
    address = 'gorkha'
    school = 'ncit'
    if username and password and address and school == '4863':
        session['entered_in'] = True
        page = jwt.encode({
            'user': username,
            'expiration': datetime.utcnow() + timedelta(seconds=120)
        }, app.config['python-key'])
        return jsonify({'page': page.decode("utf-8")})
    else:
        return make_response("Unable to verify", 402, {'WWW-Authenticate': 'Basic realm="Authentication Failed!"'})
if __name__ =='__main__':
  app.run(debug=True)
