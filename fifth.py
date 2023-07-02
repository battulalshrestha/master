from flask import Flask
from flask_restful import Api,Resource
app = Flask(__name__)
api = Api(app)
names = {"nishan":{"age":21,"address":"rautepani","college":"Ncit","Roll .No":14}}

class hello(Resource):
  def get(self,name):
    return names[name]
api.add_resource(hello,"/hello/<string:name>")
if __name__ == "__main__":
   app.run(debug=True)
  