from flask import Flask 
from flask_restful import Api,Resource
#making a app using Flask from which i import and making it using name..
app = Flask(__name__)
api = Api(app)
# using Api we create the add resource to the (Self, Init type)

# main source to run flask in server
if __name__ == "__main__":
 app.run(debug= True)


