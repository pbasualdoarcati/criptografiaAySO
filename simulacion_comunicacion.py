from pathlib import Path
from criptografia_rsa import cargar_clave_publica, cargar_clave_privada, cifrar_mensaje, descifrar_mensaje

class SimulacionComunicacion:
    def __init__(self):
        carpeta_actual = Path(__file__).parent

        self.claves = {
            "A": {
                "privada": cargar_clave_privada(carpeta_actual / "user_a_private_key.pem"),
                "publica": cargar_clave_publica(carpeta_actual / "user_a_public_key.pem")
            },
            "B": {
                "privada": cargar_clave_privada(carpeta_actual / "user_b_private_key.pem"),
                "publica": cargar_clave_publica(carpeta_actual / "user_b_public_key.pem")
            }
        }

    def enviar_mensaje(self, receptor, mensaje):
        clave_pub_receptor = self.claves[receptor]["publica"]
        return cifrar_mensaje(clave_pub_receptor, mensaje)

    def recibir_mensaje(self, receptor, mensaje_cifrado):
        clave_priv_receptor = self.claves[receptor]["privada"]
        return descifrar_mensaje(clave_priv_receptor, mensaje_cifrado)
