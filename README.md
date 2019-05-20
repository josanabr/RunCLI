# VagrantFlask

En este repositorio se encuentran una serie de scripts que pueden servir de guía para llevar a cabo el proyecto propuesto en este [video](https://www.youtube.com/watch?v=mV-Jy_xNRPU&list=PLNqsgMwXL3mE9-f669TxR-CVUgGldygl5). 
Las diapositivas del video se pueden acceder [aquí](https://docs.google.com/presentation/d/1U17A6Q79JSyPasH9u-33JbJBdFPUXC1xDaKr9EXjs2M/edit?usp=sharing)

En el video se propone el desarrollo de una herramienta que permita la gestión de máquinas virtuales desplegadas con Vagrant sobre un cluster computacional. 
Los detalles se encuentran en el video mencionado en el párrafo anterior.

# Requerimientos

Para llevar a cabo este proyecto se requiere:

* Tener conocimientos de comandos de Linux para extraer información del sistema.
* Tener conocimientos de Python pues es el lenguaje en el que se han desarrollado los scripts de este repositorio.
* Tener conocimientos de Virtualización en particular de las herramientas VirtualBox y Vagrant.
* Tener conocimientos de *Web Services* y un conocimiento del *microframework* Flask.

# Scripts

A continuación se describen una serie de scripts que pueden ser de utilidad para desarrollar el proyecto propuesto.

* [RunCLI](RunCLI.py) es un script en Python que permite la ejecucion de un comando en un sistema Unix/Linux y retorna en una cadena de caracteres lo que regularmente se ve por pantalla al ejecutar dicho comando.
