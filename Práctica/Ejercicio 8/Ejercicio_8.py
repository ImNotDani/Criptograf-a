from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import base64
from base64 import b64decode, b64encode
# Ejemplo de cifrado AES
key = get_random_bytes(32)  # AES-256
cipher = AES.new(key, AES.MODE_EAX)
tarjeta = bytes.fromhex("4231212345676891")
ciphertext, tag = cipher.encrypt_and_digest(tarjeta)

# Ejemplo de firma digital RSA
private_key = RSA.generate(2048)
public_key = private_key.publickey()
message = bytes("idUsuario: 1, usuario: José Manuel Barrio Barrio, tarjeta: ciphertext_here", "UTF-8")
hash_obj = SHA256.new(message)
signature = pkcs1_15.new(private_key).sign(hash_obj)

# Verificación de la firma
try:
    pkcs1_15.new(public_key).verify(hash_obj, signature)
    print("La firma es válida.")
except (ValueError, TypeError):
    print("La firma no es válida.")
