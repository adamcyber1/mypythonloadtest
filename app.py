from random import randint
from time import sleep

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    sleep(randint(10, 100) / 1000)

    return 'Hello, World!'