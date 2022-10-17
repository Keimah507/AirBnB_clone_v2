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
    """Returns a string at the /python/<text> route,
    with default text 'is cool', or expansion of <text>"""
    new = text.replace('_', ' ')
    return 'Python %s' % new

@app.route('/number/n', strict_slashes=False)
def number(n):
    """Returns a string at the /number/<n> route,
    only if n is an int"""
    if type(n) == int:
        return '%i is a number' % n

if __name__ == '__main__':
    app.run(host='0.0.0.0')