import requests
from flask import Flask
from flask_restful import Api,Resource
app = Flask(__name__)
api = Api(app)
vidios = {}
class Vidio (Resource):
  def get( vidio_id):
   return vidios[vidio_id]
def put(self,vidio_id):
  #request.method()
  print(requests.form['likes'])
api.add_resource(Vidio,"/Vidio/<int:vidio_id>")
  
if __name__ == "__main__":
   app.run(debug=True)
  