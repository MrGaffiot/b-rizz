from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html', render_template=render_template, len=len)

@app.route("/portraits")
def portraits():
    return render_template("portraits.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/about")
def about():
    return render_template("aboutme.html")

@app.route("/concerts")
def concerts():
    return render_template("concerts.html")

@app.route("/nightlibeznice")
def nightlibeznice():
    return render_template("nightlibeznice.html")

@app.route("/Sklepos9.9.2023")
def Sklepos992023():
    return render_template("Sklepos9.9.2023.html")

"""sumary_line
@app.route("/project/[JMENO PROJEKTU]")
def [(JMENO PROJEKTU]):
    return render_template("JMENO SOUBORU")
"""

with open("static/boris.png", "r") as file:
    print("I <3 Boris")
    print(file)

app.run()