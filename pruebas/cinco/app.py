from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola, no se tu nombre."

@app.route("/<string:name>")
def hello(name):
    return "Hola, {}".format(name)
