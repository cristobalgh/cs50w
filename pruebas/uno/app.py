import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = random.choice(["Hola!","Tanto tiempo!","Otra vez acá?"])
    consejo = random.choice(["Ten paciencia","Duerme bien","Come bien"])
    numero = random.randrange(10)
    return render_template("index.html", headline=headline, consejo=consejo, numero=numero)
