from urllib import response
from flask import Flask, request, Response, jsonify
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi'

@app.route('/fibonacci')
def US():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    print(hostname, fs_port, number, as_ip, as_port)
    if(hostname == None or fs_port == None or number == None or as_ip == None or as_port == None):
        return Response("Bad request", status = 400)

    # ip_info
    ip_info = {'name': hostname, 'fs_port': fs_port}

    # try to get response by sending get request to as server
    try:
        res = requests.get('http://' + as_ip + ':' + as_port, params=ip_info)
    except ValueError:
        return Response("bad request", status = 400)

    # error checking
    if res.status_code == 400:
        return Response("bad request", status = 400)
    if res.status_code == 404:
        return Response("hostname not found", status = 404)

    # if a valid response
    if res.status_code == 200:
        FS_server = 'http://' + res.text + ':' + fs_port + '/fabonacci?number=' + number

        # get request to fs server
        try:
            fs_res = requests.get(FS_server)
            return fs_res.text
        except ValueError:
            return Response(str(fs_res.text), status = 200)

    # if something happens, return bad request
    return Response("bad request", status = 400)


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
