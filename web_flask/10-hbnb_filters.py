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


@app.route('/hbnb_filters', strict_slashes=False)
def showFilters():
    states = storage.all('State')
    cities = storage.all('City')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
