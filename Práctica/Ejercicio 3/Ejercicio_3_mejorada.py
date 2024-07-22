import base64
from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

import jks

textoPlano = bytes('KeepCoding te enseña a codificar y a cifrar', 'UTF-8')
#Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
keystore = "C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Práctica\\Ejercicio 2\\KeyStorePracticas"
keystore_password = "123456"

# Carga keystore
keystore = jks.KeyStore.load(keystore, keystore_password)

# Obtener la clave con la etiqueta "cifrado-sim-chacha-256"
alias = "cifrado-sim-chacha20-256"
key_entry = keystore.secret_keys[alias]
clave = key_entry.key

# La clave es de 32 bytes para AES-256?
if len(clave) == 32:
    print("Clave extraída:", clave.hex())
else:
    print("La clave extraída no tiene la longitud correcta para AES-256")

datos_autenticados = bytes("","UTF-8")

#Importante NUNCA debe fijarse el nonce, en este caso lo hacemos para mostrar el mismo resultado en cualquier lenguaje.
nonce_mensaje = base64.b64decode('9Yccn/f5nJJhAt2S')

#Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
cipher.update(datos_autenticados)
texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano)

print("texto cifrado:", texto_cifrado.hex())
print("tag:" , tag.hex())









""" try:

    textoPlano = bytes('KeepCoding es una gran oportunidad de aprender muchas cosas sobre ciberseguridad', 'UTF-8')
    #Se requiere o 256 o 128 bits de clave, por ello usamos 256 bits que se transforman en 64 caracteres hexadecimales
    clave = bytes.fromhex('c936108299307d3f6f7585b96013346d043f3920b03284c6b45253fd51a545ca')
    #Importante NUNCA debe fijarse el nonce
    nonce_mensaje = get_random_bytes(12)
    #Con la clave y con el nonce se cifra. El nonce debe ser único por mensaje
    datos_asociados = bytes('Datos no cifrados sólo autenticados', 'utf-8')
    cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje)
    cipher.update(datos_asociados)
    texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano)
    #Simulamos el mensaje que se debe enviar, en este caso lo enviaremos todo el contenido en base64
    mensaje_enviado = { "nonce": b64encode(nonce_mensaje).decode(),"datos asociados": b64encode(datos_asociados).decode(), "texto cifrado": b64encode(texto_cifrado).decode(), "tag": b64encode(tag).decode()}
    json_mensaje = json.dumps(mensaje_enviado)
    print("Mensaje: ", json_mensaje)


    #Descifrado...

    decipher = ChaCha20_Poly1305.new(key=clave, nonce=b64decode(mensaje_enviado["nonce"]))
    decipher.update(datos_asociados)
    plaintext = decipher.decrypt_and_verify(b64decode(mensaje_enviado["texto cifrado"]),b64decode(mensaje_enviado["tag"]))
    print('Datos cifrados en claro = ',plaintext.decode('utf-8'))
except (ValueError, KeyError) as error: 
    print("Problemas al descifrar....")
    print("El motivo del error es: ", error) """