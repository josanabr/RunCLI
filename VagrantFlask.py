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

#
# Este metodo retorna la cadena 'hello world' retornada al ejecutar el comando
# "echo 'hello world'".
#
@app.route('/')
def helloworld():
    return jsonify(output=RunCLI.runCommand("echo 'hello world'"))

#
# Este metodo retorna el contenido del directorio al cual apunta la variable
# config.VAGRANSERVICEHOME definida en el archivo config.py
#
@app.route("/vagrant/list")
def vagrantlist():
    return jsonify(outpput=RunCLI.runCommand("ls %s"%(config.VAGRANTSERVICEHOME)))

#
# Este metodo retorna el contenido de un archivo llamado '<name>' y que se 
# encuentra en el directorio al que apunta la variable 
# config.VAGRANTSERVICEHOME.
#
# El contenido del archivo '<name>' debera contener un directorio donde 
# se ha definido una maquina virtual con la herramienta Vagrant
#
@app.route("/vagrant/located/<name>")
def vagrantlocated(name):
    return jsonify(output=RunCLI.runCommand("cat %s/%s"%(config.VAGRANTSERVICEHOME,name)))

#
# Este metodo es muy PELIGROSO y permite la ejecucion de un comando arbitrario
# en un sistema Unix/Linux.
#
@app.route("/run/<command>")
def runCommand(command):
    return jsonify(output=RunCLI.runCommand(command))

