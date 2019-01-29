#!/usr/bin/python3
"""Module"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def db_close(self):
    """close session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def showStates():
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def showCities(id):
    states = storage.all('State')
    key = "{}.{}".format('State', id)
    state = states[key]
    cities = storage.all('City')
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
