#!/usr/bin/env python3
"""
Script para desencriptar contraseñas de DbVisualizer
DbVisualizer usa PBEWithMD5AndDES con una clave estática
"""

import base64
from hashlib import md5
from Crypto.Cipher import DES

# Constantes hardcodeadas en DbVisualizer
ITERATIONS = 10
SALT = b'\x8E\x12\x39\x9C\x07\x72\x6F\x5A'
PASSWORD = 'qinda'

class PBEWithMD5AndDES:
    def __init__(self, password, salt, iterations):
        key = self._generate_key(password, salt, iterations, 16)
        self.key = key[:8]
        self.iv = key[8:16]

    def _cipher(self):
        return DES.new(self.key, DES.MODE_CBC, self.iv)

    def _generate_key(self, password, salt, count, length):
        key = password.encode() + salt
        for i in range(count):
            key = md5(key).digest()
        return key[:length]

    def decrypt(self, ciphertext):
        plaintext = self._cipher().decrypt(ciphertext)
        padding = plaintext[-1]
        return plaintext[:-padding].decode('utf-8')

def decrypt_password(encrypted_password):
    """Desencripta una contraseña encriptada de DbVisualizer"""
    pbe = PBEWithMD5AndDES(PASSWORD, SALT, ITERATIONS)
    decoded = base64.b64decode(encrypted_password)
    return pbe.decrypt(decoded)

if __name__ == "__main__":
    # Contraseña encriptada encontrada en el archivo de configuración
    encrypted = "QCs2yHiIcLRGUJ+zYqEZLw=="

    try:
        decrypted = decrypt_password(encrypted)
        print("\n" + "="*60)
        print("CREDENCIALES DESENCRIPTADAS - ALMA (IRIS)")
        print("="*60)
        print(f"Servidor: 10.63.180.25:51773")
        print(f"Base de datos: LIVE-CLOV")
        print(f"Usuario: 18233087-6")
        print(f"Contraseña: {decrypted}")
        print("="*60)
    except Exception as e:
        print(f"Error al desencriptar: {e}")
        print("Asegúrate de tener instalado pycryptodome: pip install pycryptodome")
