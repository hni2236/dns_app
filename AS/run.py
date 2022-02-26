from audioop import add
from flask import Flask, Response, jsonify, request
import json
import os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def AS():

    file = "address.json"
    if not os.path.exists(file):
        os.system(r'touch address_map.json')
        file = 'address.json'
    
    if request.method == 'POST':
        data = request.form
        print(data)
        hostname = data['name']
        address = data['address']
        d = {}
        d[hostname] = address
        with open(file, 'w') as json_file:
            json.dump(d, json_file)
        return Response("Registered", status = 201)

    if request.method == 'GET':
        key = request.args.get('name')
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            if key not in data:
                return Response("hostname not found", status = 404)
            else:
                address = data.get(key)
                return Response(address, status = 200)


app.run(host='0.0.0.0',
        port=53533,
        debug=True)