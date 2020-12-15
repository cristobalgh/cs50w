from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """hola que tal"""
    return "Hello, world!"

@app.route("/cristobal")
def cristobal():
    return "Hola cristobal!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"
