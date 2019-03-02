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

@app.route('/vms/ram/<name>', methods=['GET'])
def get_vmRam(name):
    return helpers.vmShowRam(name)

@app.route('/vms/numCPUs/<name>', methods=['GET'])
def get_vmNumCpus(name):
    return helpers.vmShownumCpus(name)

@app.route('/vms/numCards/<name>', methods=['GET'])
def get_vmNumCards(name):
    return helpers.vmShowNumCards(name)

@app.route('/vms/set/numCPUs/<name>/<int:num>', methods=['PUT'])
def set_vmCpus(name,num):
    return helpers.vmSetNumCards(name,num)

@app.route('/vms/set/<name>/vmRAM/<int:num>', methods=['PUT'])
def set_vmRAM(name,num):
    return helpers.vmSetRAM(name,num)
 
@app.route('/vms/set/<name>/%CPU/<int:num>', methods=['PUT'])
def set_vmPercentageCpu(name,num):
    return helpers.vmSetPercentageCpu(name,num)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
