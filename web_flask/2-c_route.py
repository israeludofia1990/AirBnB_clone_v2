#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask


app = Flask = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_nbnb():
    '''default route'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    '''hbnb_route'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_route(text=None):
    '''C route'''
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
