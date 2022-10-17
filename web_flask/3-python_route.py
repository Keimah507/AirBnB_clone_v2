#!/usr/bin/python3
"""Starts up a Flask web application"""

from flask import Flask
app=Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_alx():
    """Returns a string at the root route"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string at the hbnb route"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Returns a string at the /c/<text> route,
    expands the <text> variable"""
    new = text.replace('_', ' ')
    return 'C %s' % new

@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text):
    """Returns a string at the /python/<text>route,
    with a default text of 'is cool',
    or expansion of the <text> variable"""
    new = text.replace('_', ' ')
    return 'Python %s' % new

if __name__ == '__main__':
    app.run(host='0.0.0.0')