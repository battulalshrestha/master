
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
    app.run(debug=True)
