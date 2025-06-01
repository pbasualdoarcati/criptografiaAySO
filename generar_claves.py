from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path

def generar_y_guardar_claves(nombre_usuario):
    # Directorio donde está este script
    carpeta_actual = Path(__file__).parent
    
    # Generar clave privada
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    
    # Guardar clave privada en carpeta_actual
    ruta_privada = carpeta_actual / f"{nombre_usuario}_private_key.pem"
    with open(ruta_privada, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Extraer y guardar clave pública en carpeta_actual
    public_key = private_key.public_key()
    ruta_publica = carpeta_actual / f"{nombre_usuario}_public_key.pem"
    with open(ruta_publica, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

# Generar claves para los dos usuarios
generar_y_guardar_claves("user_a")
generar_y_guardar_claves("user_b")
