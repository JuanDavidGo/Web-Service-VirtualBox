#!/usr/bin/python
import helpers
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

@app.route('/vms', methods=['GET'])
def get_vms():
 return helpers.listVMSToJSON()

@app.route('/vmsrunning', methods=['GET'])
def get_vmsRunning():
    return helpers.listVMSToJSONRunning()

@app.route('/vms/<name>', methods=['GET'])
def get_vmsInfo(name):
    return helpers.vmsInfo(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)