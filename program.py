from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>cs more</p>"


@app.route("/page")
def page():
    return "<h1>page! page! page!</h1>"