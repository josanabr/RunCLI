#!/usr/bin/env python
#
# Este script en Python asume la ejecucion del web service VagrantFlask.py
#
# Para mas detalles de como se ejecuta este web service leer el script 
# VagrantFlask.py
#
# Author: John Sanabria - john.sanabria@correounivalle.edu.co
# Date: 2019_05_19
#
import requests
import json

#
# Se hace el acceso al URI '/run' y se le pasa como argumento el comando
# 'vboxmanage list vms'. Este comando se puede ejecutar regularmente en una 
# terminal de Unix/Linux en la cual esta instalado el programa VirtualBox.
#
# La respuesta del web service es almaceando en la variable 'r'
#
r = requests.get("http://localhost:5000/run/vboxmanage%20list%20vms")
print("r es de tipo %s y r.text es de tipo %s"%(type(r),type(r.text)))

#
# De la variable 'r' se toma el atributo 'text' y se guarda en la variable
# data.
#
data = json.loads(r.text)
print("data de tipo %s"%(type(data)))

#
# De la variable 'data' que es una lista llave/valor se procesa el valor de la
# llave 'output' y se parte por el caracter '\n' o salto de linea.  
#
# Vale la pena mencionar que lo que arrojan los web services de VagrantFlask es
# un dato en formato JSON con una llave/valor. La llave es 'output'.
#
x = data['output'].split('\n')
for i in x: # Se muestran todas las lineas resultado de ejecutar el comando 'vboxmanage'
    print(i)
