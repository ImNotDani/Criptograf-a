from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512
import secrets
import jks
import base64
from base64 import b64encode, b64decode
# Ruta keystore
keystore_path = "C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Cripto en flujo\\KeyStorePracticas"
keystore_password = "123456"

# Carga keystore
keystore = jks.KeyStore.load(keystore_path, keystore_password)

# Obtener la clave con la etiqueta "cifrado-sim-chacha-256"
alias = "cifrado-sim-aes-256"
key_entry = keystore.secret_keys[alias]
clave = key_entry.key

# La clave es de 32 bytes para AES-256?
if len(clave) == 32:
    print("Clave extraída:", clave.hex())
else:
    print("La clave extraída no tiene la longitud correcta para AES-256")



salt = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")
master_secret = secrets.token_bytes(64)
key1 = HKDF(clave, 32, salt, SHA512, 1)
key1_b64 = base64.b64encode(key1).decode()

print("Clave AES(hex): ", key1.hex())
print("Clave AES(b64): ", key1_b64)

