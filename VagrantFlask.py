#!/usr/bin/env python
#
# Este script en Python permite la ejecucion de algunos comandos de Linux
# los cuales se exponen como servicios API REST
#
# Para ejecutar este script debe ejecutar los siguientes pasos:
#  virtualenv venv
#  . venv/bin/activate
#  pip install Flask
#  export FLASK_APP=VagrantFlask.py
#  flask run
#
# Author: John Sanabria - john.sanabria@correounivalle.edu.co
# Fecha: 2019-05-17
#
from flask import Flask, jsonify
import RunCLI
import config

app = Flask(__name__)


@app.route('/')
def helloworld():
    return jsonify(output=RunCLI.runCommand("echo 'hello world'"))

@app.route("/vagrant/list")
def vagrantlist():
    return jsonify(outpput=RunCLI.runCommand("ls %s"%(config.VAGRANTSERVICEHOME)))

@app.route("/vagrant/located/<name>")
def vagrantlocated(name):
    return jsonify(output=RunCLI.runCommand("cat %s/%s"%(config.VAGRANTSERVICEHOME,name)))

@app.route("/run/<command>")
def runCommand(command):
    return jsonify(output=RunCLI.runCommand(command))

