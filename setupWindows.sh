#!/bin/bash
# Crear el entorno virtual en la carpeta .venv
python -m venv .venv
# Activar el entorno virtual (en bash de Windows)
source .venv/Scripts/activate
# Instalar las dependencias del archivo requirements.txt
pip install -r requirements.txt
