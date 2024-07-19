from Crypto.Hash import HMAC, SHA256, SHA512

import jks
# Ruta keystore
keystore_path = "C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Práctica\\Ejercicio 2\\KeyStorePracticas"
keystore_password = "123456"

# Carga keystore
keystore = jks.KeyStore.load(keystore_path, keystore_password)

# Obtener la clave con la etiqueta "cifrado-sim-chacha-256"
alias = "hmac-sha256"
key_entry = keystore.secret_keys[alias]
clave = key_entry.key

# La clave es de 32 bytes para AES-256?
if len(clave) == 32:
    print("Clave extraída:", clave.hex())
else:
    print("La clave extraída no tiene la longitud correcta")

mensaje = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.", "UTF-8")
hmac256 = HMAC.new(clave,msg=mensaje,digestmod=SHA256)
result = "KO"
try:
        hmac256.hexverify(hmac256.hexdigest())
        result = "OK"
except ValueError:
        result = "KO"
print("result: " + result)

# def getHMAC(key_bytes,data_bytes):
#     hmac256 = HMAC.new(key_bytes, msg=data_bytes, digestmod=SHA256)
#     return hmac256.hexdigest()

# def validateHMAC(key_bytes,data_bytes,hmac):
#     hmac256 = HMAC.new(key_bytes,msg=data_bytes,digestmod=SHA256)
#     result = "KO"
#     try:
#         hmac256.hexverify(hmac)
#         result = "OK"
#     except ValueError:
#         result = "KO"
#     print("result: " + result)
#     return result


# clave_bytes = bytes.fromhex('c936108299307d3f6f7585b96013346d')
# datos = bytes("KeepCoding mola un montón", "utf8")

# hmac = getHMAC(clave_bytes,datos)

# print(hmac)

# print(validateHMAC(clave_bytes, datos,hmac))