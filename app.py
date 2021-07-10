from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Brave new world {}".format(os.environ['AUTHOR_NAME'])
