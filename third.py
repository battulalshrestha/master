from flask import Flask 
from flask_restful import Api,Resource
app = Flask(__name__)
api = Api(app)
class pyapp(Resource):
  def get(self):
   return {"data":"pyapp"}
api.add_resource(pyapp,"/pyapp")
if __name__ == "__main__":
   app.run(debug = True)
