#!/usr/bin/python3
"""Runs simple flask application with the following routes:
/
/hbnb
/c/<text>
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """Home route"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb():
    """hbnb route"""
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """c is fun route"""
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
