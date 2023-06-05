from random import randint
from time import sleep

from flask import Flask
app = Flask(__name__)

@app.route('/')
def simulated_request():
    sleep(randint(100, 1000) / 1000)
    return 'Returned!'

