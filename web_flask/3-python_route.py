#!/usr/bin/python3
"""Module"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns Hello HBNB"""
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    """returns text"""
    new_text = text.replace('_', ' ')
    return("C {}".format(new_text))


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_text_python(text):
    """returns Python and text"""
    new_text = text.replace('_', ' ')
    return("Python {}".format(new_text))


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
