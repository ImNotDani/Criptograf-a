import base64
from base64 import b64decode, b64encode
import jks
import os
from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


# Obteniendo el path
path = os.path.dirname(__file__)
keystore = "C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Práctica\\Ejercicio 2\\KeyStorePracticas"
ks = jks.KeyStore.load(keystore, "123456")

for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        key = sk.key

iv = bytes.fromhex("00000000000000000000000000000000")

dato_cifrado = base64.b64decode("TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=")
cipher = AES.new(key, AES.MODE_CBC, iv)
mensaje_des_bytes = unpad(cipher.decrypt(dato_cifrado), AES.block_size, style="pkcs7")
print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))