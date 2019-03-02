#!/usr/bin/python
import subprocess
from flask import Flask, jsonify, abort, make_response, request

def listVMSToJSON():
    p = subprocess.Popen("VBoxManage list vms", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err != None:
        abort(404)
        
    strList = output.decode("utf-8")
    splittedStr = strList.split()
    if len(splittedStr) == 0:
        abort(204)

    machineList = []

    for index in range(0, len(splittedStr), 2):
        if index + 1 < len(splittedStr):
            machine = {
            'name': splittedStr[index],
            'id': splittedStr[index+1]
        }
        machineList.append(machine)
    
    return jsonify({'machineList': machineList})

def listVMSToJSONRunning():
    p = subprocess.Popen("VBoxManage list runningvms", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    if err != None:
        abort(404)
        
    strList = output.decode("utf-8")
    splittedStr = strList.split()
    if len(splittedStr) == 0:
        abort(204)

    machineList = []

    for index in range(0, len(splittedStr), 2):
        if index + 1 < len(splittedStr):
            machine = {
            'name': splittedStr[index],
            'id': splittedStr[index+1]
        }
        machineList.append(machine)
    
    return jsonify({'machineList': machineList})

def vmsInfo(name):
    p= subprocess.check_output(['VBoxManage', 'showvminfo', name ])
    
    vm = p.decode("utf-8")
    splittedStr = vm.split()

    return jsonify({'Vmachine' : splittedStr})
