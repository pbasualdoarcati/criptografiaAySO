from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization

def cargar_clave_publica(ruta_archivo):
    with open(ruta_archivo, "rb") as f:
        return serialization.load_pem_public_key(f.read())

def cargar_clave_privada(ruta_archivo):
    with open(ruta_archivo, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)
    
def cifrar_mensaje(clave_publica, mensaje):
    mensaje_bytes = mensaje.encode("utf-8")
    mensaje_cifrado = clave_publica.encrypt(
        mensaje_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensaje_cifrado

def descifrar_mensaje(clave_privada, mensaje_cifrado):
    mensaje_descifrado = clave_privada.decrypt(
        mensaje_cifrado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensaje_descifrado.decode("utf-8")
