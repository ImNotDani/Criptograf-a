from Crypto.Cipher import ChaCha20
from base64 import b64decode, b64encode
import base64
import Crypto.Cipher
import Crypto.Util.Padding
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales

import jks
# Ruta keystore
keystore = "C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Práctica\\Ejercicio 2\\KeyStorePracticas"
keystore_password = "123456"

# Carga keystore
keystore = jks.KeyStore.load(keystore_path, keystore_password)

# Obtener la clave con la etiqueta "cifrado-sim-chacha-256"
alias = "cifrado-sim-chacha20-256"
key_entry = keystore.secret_keys[alias]
clave = key_entry.key

# La clave es de 32 bytes para AES-256?
if len(clave) == 32:
    print("Clave extraída:", clave.hex())
else:
    print("La clave extraída no tiene la longitud correcta para AES-256")

clave2 = bytes.fromhex("af9df30474898787a45605ccb9b936d33b780d03cabc81719d52383480dc3120")
#Importante NUNCA debe fijarse el nonce, en este caso lo hacemos para mostrar el mismo resultado en cualquier lenguaje.
nonce = base64.b64decode("9Yccn/f5nJJhAt2S")
print('nonce  = ', nonce.hex())

#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = ChaCha20.new(key=clave2, nonce=nonce)
texto_cifrado = cipher.encrypt(textoPlano)
print('Mensaje cifrado en HEX = ', texto_cifrado.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado).decode())


#Descifrado...
decipher = ChaCha20.new(key=clave2, nonce=nonce)
plaintext = decipher.decrypt(texto_cifrado)
print('Mensaje en claro = ',plaintext.decode('utf-8'))


#nonce  =  fbdbffb77f5966b2
#Mensaje cifrado en HEX =  bbc80c978117d14a0d08e01e84fcbfa30f5af52d7e2fb27ef9c995cb16621ce89f1726f8264fad31c8bc80edde320f4a64e0c904b211d2259edc6dab2b346c8ec744ab05501ae8132f043dd15842de94d2ec150760514123deaf4e6b0bca
#Mensaje cifrado en B64 =  u8gMl4EX0UoNCOAehPy/ow9a9S1+L7J++cmVyxZiHOifFyb4Jk+tMci8gO3eMg9KZODJBLIR0iWe3G2rKzRsjsdEqwVQGugTLwQ90VhC3pTS7BUHYFFBI96vTmsLyg==
#Mensaje en claro =  Cualquier desarrollador que use este libro será capaz de cifrar y descifrar con poco esfuerzo