#!/usr/bin/python3
"""Module"""
from collections import OrderedDict
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def db_close(self):
    """close session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def showCities():
    """show all cities from a state"""
    states = storage.all('State')
    cities = storage.all('City')
    return render_template('8-cities_by_states.html', states=states, cities=cities)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
