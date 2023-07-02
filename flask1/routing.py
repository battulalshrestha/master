'''from markupsafe import Flask,escape
app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'   '''
from flask import Flask

app = Flask(__name__)

@app.route('/nishan/<nishan01>')
def show_user_profile(nishan01):
    # show the user profile for that user
    return f'{nishan01}'

@app.route('/facebook/<int:messenger>')
def show_post(messenger):
    # show the post with the given id, the id is an integer
    return f'facebook {messenger}'

@app.route('/http:<path:http_00001>')
def show_subpath(http_00001):
    # show the subpath after /http:00001/
    return f'http:00001/{http_00001}'

if __name__ == "__main__":
    app.run(debug=True)
