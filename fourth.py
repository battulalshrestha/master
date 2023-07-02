from flask import Flask
from flask_restful import Resource,Api
app = Flask(__name__)
api = Api(app)
class hellonishan(Resource):
  def host(self):
    return {"hosted":"hellonishan"}
api.add_resource(hellonishan,"/hellonishan")
if __name__ == "__main__":
   app.run(debug=True)
  