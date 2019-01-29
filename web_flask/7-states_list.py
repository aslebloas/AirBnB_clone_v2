#!/usr/bin/python3
"""Module"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def db_close(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def showStates():
    """show all states"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
