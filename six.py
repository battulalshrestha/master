from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask website!'

@app.route('/about')
def about():
    return 'This is the About page.'

@app.route('/contact')
def contact():
    return 'This is the Contact page.'

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/template')
def render_template():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
