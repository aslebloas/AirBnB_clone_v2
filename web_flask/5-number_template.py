#!/usr/bin/python3
"""Module"""
from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """returns n is a number or not"""
    if isinstance(n, int):
        return("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def templating(n):
    """returns n is a number or not"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
