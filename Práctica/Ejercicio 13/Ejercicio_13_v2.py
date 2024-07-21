from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii
import os

fichero_pub = "C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Hashing\\clave-rsa-oaep-publ.pem"
f=open(fichero_pub,'r')
keypub= RSA.import_key(f.read())

fichero_priv = "C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Hashing\\clave-rsa-oaep-priv.pem"
f=open(fichero_priv,'r')
keypriv= RSA.import_key(f.read())


# Firma del mensaje con PKCS#1 v1.5 esquema de firma (RSASP1)
msg = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.", "UTF-8")
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(keypriv)
signature = signer.sign(hash)
print("Firma:", signature.hex())

# Vericar la firma con PKCS#1 v1.5 (RSAVP1)
msg = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.", "UTF-8")
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(keypub)
try:
    verifier.verify(hash, signature)
    print("Firma válida.")
except:
    print("Firma invalida.")

# # Verificación inválida PKCS#1 v1.5 signature (RSAVP1)
# msg = bytes('Asumamos el error de cara a los organismos oficiales.','utf8')
# hash = SHA256.new(msg)
# verifier = PKCS115_SigScheme(keypub)
# try:
#     verifier.verify(hash, signature)
#     print("Firma válida.")
# except:
#     print("Firma invalida.")