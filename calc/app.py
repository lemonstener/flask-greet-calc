from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def addition():
    '''Add a and b together'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)

    return str(result)


@app.route('/sub')
def subtraction():
    '''Subtract b from a'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a, b)

    return str(result)


@app.route('/mult')
def multiplication():
    '''Multiply a by b'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a, b)

    return str(result)


@app.route('/sub')
def division():
    '''Divide a by b'''
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a, b)

    return str(result)
