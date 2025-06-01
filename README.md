<p align="center">
  <img src="assets/logo-utn.png" alt="Logo UTN" width="100%"/>
</p>
<p align="center">
  <strong>Universidad Tecnológica Nacional</strong>
</p>

# Semana de Integración 2 - Conjuntos Numéricos y Python

## Introducción

Completar

---

## Integrantes (ordenados alfabéticamente)

- **Pablo Basualdo Arcati**
- **Dante Kaddarian**

---

## Consignas
Completar
### 
---

### Estructura del proyecto
<pre>
📦 
├── main.py                      # Script principal que ejecuta el programa
├── requirements.txt             # Lista de dependencias a instalar con pip
├── README.md                    # Instrucciones y documentación del proyecto
├── setup.sh                     # Script para automatizar instalación en Linux/macOS
├── setup.ps1                    # Script para automatizar instalación en Windows PowerShell
└── utils/                       # Módulo con funciones auxiliares
    ├── __init__.py              # Inicializa el paquete utils
    ├── criptografia_rsa.py      # Funciones para cargar la clave privada y publica, cifrar y descifrar mensajes
    ├── generar_claves.py        # Funciones para crear claves publicas y privadas
    ├── simular_comunicacion.py  # Funciones que simular una comunicación entre dos usuarios donde se envia y recepciona mensajes, utilizando clases
    ├── simular_carga.py         # Funciones para simular una demora en el envio del mensaje y hacerlo un poco más realista
    ├── simular_sniffer.py       # Función para simular una intercepción por un sniffer que lee el mensaje encriptado
</pre>

---

### Herramientas externas - Documentación
`cryptography`: https://cryptography.io/en/latest/

---

## Setup del entorno y dependencias

### 1. Crear y activar entorno virtual

Desde la raíz del proyecto, abrir una terminal y ejecutar:

#### En Windows (PowerShell):

python -m venv .venv

O ejectuar script: setup.ps1


#### En Linux / macOS:

python3 -m venv .venv

O ejecutar bash: bash setup.sh

---

#### Check:

Comprobar si las dependencias de requirements.txt se encuentran instaladas, caso contrario python install <cryptography>