from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.exceptions import InvalidSignature
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

# Mensaje a firmar
mensaje = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.","UTF-8")

# Firmar con ed25519
# Leer clave privada ed25519 en modo binario
with open("C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Práctica\\Ejercicio 13\\ed25519-priv", "rb") as f:
    private_key_bytes = f.read()
    ed25519_private_key = Ed25519PrivateKey.from_private_bytes(private_key_bytes)

# Firmar el mensaje
ed25519_signature = ed25519_private_key.sign(mensaje)

# Convertir la firma a hexadecimal
ed25519_signature_hex = binascii.hexlify(ed25519_signature).decode()

print("Firma RSA PKCS#1 v1.5 (hex):", rsa_signature_hex)
print("Firma ed25519 (hex):", ed25519_signature_hex)

# Verificación (opcional)
# Leer clave pública ed25519 en modo binario
with open("C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Práctica\\Ejercicio 13\\ed25519-publ", "rb") as f:
    public_key_bytes = f.read()
    ed25519_public_key = Ed25519PublicKey.from_public_bytes(public_key_bytes)

try:
    ed25519_public_key.verify(ed25519_signature, mensaje)
    print("Firma ed25519 verificada correctamente")
except InvalidSignature:
    print("Error validando la firma ed25519")
