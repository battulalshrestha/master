# for this i have to install flask like, pip install flask in terminal 
from flask import  Flask
# i would like to give temple_run as a app name using flask  __name__ meaning is the especial variable where we can use it to __main__ fxn .
temple_run = Flask(__name__)
# for url we can use the app route like 
@temple_run.route('/man')#route name inner of the /
def run_by_men(walk):
    return "run by man"
if __name__ == "__main__":
 temple_run.run(debug=True)

