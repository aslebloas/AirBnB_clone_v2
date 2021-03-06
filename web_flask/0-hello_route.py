#!/usr/bin/python3
"""Module"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Index method returns Hello HBNB!"""
    return("Hello HBNB!")


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
