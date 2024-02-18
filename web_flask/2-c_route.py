#!/usr/bin/python3
"""
start flask application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return hello hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """return C is fun"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
