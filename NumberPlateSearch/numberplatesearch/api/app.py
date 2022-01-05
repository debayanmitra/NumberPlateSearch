import time
from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    return ('Welcome to Number Plate Search Application')


@app.route('/time')
def get_current_time():
    return {'Current time ': time.time()}


@app.route('/getNumber')
def getNumber():
    return ('Car Number')
