from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi'

@app.route('/register')
def register():
    as_port = '53533'
    hostname = request.args.get('hostname')
    ip_address = '0.0.0.0'
    d = {}
    d['name'] = hostname
    d['address'] = ip_address
    print(d)
    res = requests.post('http://0.0.0.0:53533', data = d)
    return res.text

@app.route('/fabonacci')
def fabonacci():
    number = request.args.get('number')
    res = fib_solver(int(number))
    return Response("The answer for number: " + str(res) + " is: " + str(res), status = 200)

def fib_solver(number):
    if number <= 0:
        return 0
    if number == 1:
        return 1
    return fib_solver(number - 1) + fib_solver(number - 2)



app.run(host='0.0.0.0',
        port=9090,
        debug=True)