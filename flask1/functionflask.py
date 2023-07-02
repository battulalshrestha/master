from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route('/')
def page():
  return "Hello! THIS IS THE MY FIRST PAGE<h1>hello<h1>"
@app.route("/name>")
def user(name):
  return f'hello {name}!'
@app.route('/admin')
def admin():
  return(redirect(url_for('page')))


if __name__ == '__main__':
  app.run(debug = True)