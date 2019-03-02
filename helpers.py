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
    splittedStr = vm.splitlines()

    return jsonify({'Vmachine' : splittedStr})

def vmShowRam(name):
    output = subprocess.Popen(['VBoxManage', 'showvminfo', vm ], stdout = subprocess.PIPE)
    ram = subprocess.check_output(['grep', 'Memory'], stdin = output.stdout)
    vmRam = ram.splitlines()
    return jsonify({'VmRam': vmRam})

def vmShownumCpus(name):
    output = subprocess.Popen(['VBoxManage', 'showvminfo', vm ], stdout = subprocess.PIPE)
    cpus = subprocess.check_output(['grep', 'CPUs'], stdin = output.stdout)
    vmCpus = cpus.splitlines()
    return jsonify({'VmNumberCpus': vmCpus})

def vmShowNumCards(name):
    output = subprocess.Popen(['VBoxManage', 'showvminfo', vm ], stdout = subprocess.PIPE)
    cards = subprocess.check_output(['grep', 'NCI'], stdin = output.stdout)
    enabled = subprocess.Popen(['grep', 'MAC'], stdin = cards.stdout, stdout = subprocess.PIPE)
    num = subprocess.check_output(['wc', '-l'], stdin = enabled.stdout)
    return jsonify({'VmNumberNCI': num})

def vmSetNumCards(name,num):
    subprocess.run(['vboxmanage', 'modifyvm', name, '--cpus' , num ])

    return "Se ha modificado el numero de CPUs de la maquina virtual"

def vmSetRAM(name,num):
    subprocess.run(['vboxmanage', 'modifyvm', name, '--memory' , num ])

    return "Se ha modificado el numero de la RAM de la maquina virtual"

def vmSetPercentageCpu(name,num):
    subprocess.run(['vboxmanage', 'modifyvm', name, '--cpuexecutioncap' , num ])

    return "Se ha modificado el porcentaje del procesador que se le asigna a la maquina virtual"
