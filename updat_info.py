from flask import Flask,request
app = Flask(__name__)
FACEBOOK_API_KEY = 
MESSENGER_API_KEY = '6071315356:AAGZaoJoOcEwFiYiKMpHil_HM2VpKN6gYiI'
@app.route('/deactivate_facebook', methods=['POST'])
def deactive_facebook():
    user_id = request.form.get('Battu001')
    update_info = request.form.get('update_info')
    return 'Facebook account deactivated. Instagram information updated.'
if __name__ == "__main__":
  app.run(debug = True)
