<p align="center">
  <img src="assets/logo-utn.png" alt="Logo UTN" width="100%"/>
</p>
<p align="center">
  <strong>Universidad Tecnológica Nacional</strong>
</p>

# Semana de Integración 2 - Conjuntos Numéricos y Python

## Introducción

La criptografía es una de las herramientas fundamentales dentro de la ciberseguridad. La función principal es la de proteger y asegurar la inviolabilidad de la información. 
Si contamos la historia de la criptografía podemos remitirnos a la Edad media, con los primeros Criptex, pero el marco teórico del proyecto no es el lugar para la historia, solo diremos que la criptografía puede dividirse en criptografía simetría y asimétrica, nosotros vamos a trabajar con la criptografía asimétrica, creada por Whitfield Diffie y Martin Hellman en 1976, ésta técnica criptográfica requiere que los usuarios, remitente y receptor, tengan en su poder un par de claves secretas, una publica que sirve para encriptar la información, que puede ser difundida de manera libre y otra privada, cuya función es la de descifrar el mensaje, esta ultima resulta imperioso mantenerla en secreto y guardad, ya que por lógica, si el atacante tiene acceso a ella puede descifrar nuestro mensaje.
El algoritmo de cifrado más conocido en criptografía simétrica es el creado en 1977 por Rivest, Shamir y Adleman, también llamado RSA. La seguridad de RSA esta basada en la dificultad de factorizar grandes números compuestos por números primos. Mientras no se logre resolver de manera eficiente este problema, el algoritmo continúa siendo eficaz y seguro.
En la actualidad, RSA es utilizado tanto en las transacciones bancarias como en la navegación por HTTPS.
En redes públicas donde la exposición a probables ataques es muy alta, cualquier tercero con malas intenciones puede interceptar el mensaje que se envía entre dos puntos, como lo hicimos nosotros con Python.
Nuestro proyecto simulará una comunicación entre dos usuarios donde se enviarán y decepcionará mensajes y en el medio se simulará una intercepción con un sniffer, para poder aplicar el concepto de criptografía utilizamos la librería  “Cryptography” , una librería que se encarga de cifrar y descifrar información a partir de un par de claves de tipo .pem, durante el desarrollo del programa nos encontramos con la necesidad de entender cómo funciona la librería y que clase de hash es usado y si cumple con nuestro objetivo.


---

## Integrantes (ordenados alfabéticamente)

- **Pablo Basualdo Arcati**
- **Dante Kaddarian**

---

## Consignas
Desarrollar una aplicación que simule la comunicación entre dos puntos y una intercepción del mensaje encriptado.
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

Comprobar si las dependencias de requirements.txt se encuentran instaladas, caso contrario python install cryptography