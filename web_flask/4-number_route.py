#!/usr/bin/python3
"""Runs simple flask application with the following routes:
/
/hbnb
/c/<text>
/python/<text>
/number/<n>
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


@app.route("/python")
@app.route("/python/<text>")
def python_is_fun(text="is cool"):
    """python route"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>")
def is_number(n):
    """number route"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
