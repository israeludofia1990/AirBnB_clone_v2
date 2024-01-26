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


@app.route('/c/<string:text>', strict_slashes=False)
def text(text=None):
    '''Dynamic inputed text: replace _ for space and show text'''
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_flash=False)
def python_route(text='is cool'):
    '''display “Python ”, followed by the value of the text variable'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def integer_route(n=None):
    '''integer route'''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
