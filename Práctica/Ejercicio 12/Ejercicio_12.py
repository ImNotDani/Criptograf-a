import json
import base64
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

#Cifrado
textoPlano_bytes = bytes('He descubierto el error y no volveré a hacerlo mal', 'UTF-8')
#Se puede generar aleatoriamente una clave de 16 bytes.
#clave = get_random_bytes(16)
clave = bytes.fromhex('E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74')
nonce = base64.b64decode('9Yccn/f5nJJh')
datos_asociados_bytes = bytes("Esto nos valdrá para validar la integridad y la autenticación pero nunca la confidencialidad.", "UTF-8")
cipher = AES.new(clave, AES.MODE_GCM,nonce=nonce)
cipher.update(datos_asociados_bytes)
texto_cifrado_bytes, tag = cipher.encrypt_and_digest(textoPlano_bytes)
print("Texto cifrado hex:", texto_cifrado_bytes.hex())


#Si se generase de forma automática, por no especificarlo en la llamada, se recuperaría así.
nonce_b64 = b64encode(cipher.nonce).decode('utf-8')
texto_cifrado_b64 = b64encode(texto_cifrado_bytes).decode('utf-8')
datos_asociados_b64 = b64encode(datos_asociados_bytes).decode('utf-8')
tag_b64 =b64encode(tag).decode('utf-8')
print("Texto cifrado b64: ", texto_cifrado_b64)

#Descifrado

# try:
#     b64 = json.loads(mensaje_json)
#     nonce_desc_bytes = b64decode(b64['nonce'])
#     texto_cifrado_bytes = b64decode(b64['texto cifrado'])
#     tag_desc_bytes = b64decode(b64['tag'])
#     datos_asociados_desc_bytes = b64decode(b64['datos asociados'])

#     cipher = AES.new(clave, AES.MODE_GCM, nonce=nonce_desc_bytes)
#     cipher.update(datos_asociados_bytes)
#     mensaje_des_bytes = cipher.decrypt_and_verify(texto_cifrado_bytes,tag_desc_bytes)
#     print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))

# except (ValueError, KeyError) as error:
#     print('Problemas para descifrar....')
#     print("El motivo del error es: ", error) 
