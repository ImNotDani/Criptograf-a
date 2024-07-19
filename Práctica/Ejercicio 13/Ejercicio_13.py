from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes



import os

fichero_pub = "C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Hashing\\clave-rsa-oaep-publ.pem"
f=open(fichero_pub,'r')
keypub= RSA.import_key(f.read())

fichero_priv = "C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Hashing\\clave-rsa-oaep-priv.pem"
f=open(fichero_priv,'r')
keypriv= RSA.import_key(f.read())

plaintext = bytes("El equipo está preparado para seguir con el proceso, necesitaremos más recursos.", "UTF-8")

cipher = PKCS1_v1_5.new(keypub)
ciphertext = cipher.encrypt(plaintext)
print(ciphertext.hex())

cipher = PKCS1_v1_5.new(keypriv)
decrypted_text = cipher.decrypt(ciphertext, sentinel=get_random_bytes(16))
print(decrypted_text.decode("utf-8"))

""" El descifrado de PKCS#1 v1.5 es intrínsecamente vulnerable a los ataques de tiempo (véase el ataque de Bleichenbacher). Utilice en su lugar PKCS#1 OAEP.

Esta implementación intenta mitigar el riesgo con algunas construcciones de tiempo constante. Sin embargo, no son suficientes por sí mismas: el tipo de protocolo que implementes y la forma en que manejes los errores marcan una gran diferencia.

En concreto, debes hacer que sea muy difícil para la parte (maliciosa) que envió el texto cifrado entender rápidamente si el descifrado tuvo éxito o no.

Para ello, se recomienda que tu protocolo sólo cifre textos planos de longitud fija (expected_pt_len), que el centinela sea una cadena de bytes aleatoria de la misma longitud, y que el procesamiento continúe durante el mayor tiempo posible incluso si el centinela es devuelto (es decir, en caso de descifrado incorrecto). """