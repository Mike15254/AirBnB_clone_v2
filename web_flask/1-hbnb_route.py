#!/usr/bin/python3
"""Runs simple flask application with the following routes:
/
/hbnb
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


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
