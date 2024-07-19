from ssl import VerifyFlags
import jwt
# #Generamos claves RSA
# #openssl genrsa -out private2.pem 2048
# #openssl rsa -in private.pem -pubout -out public.pem

# #Mejor leerlo desde ficheros para evitar problemas de formato en entrada de claves
# public_key = open("public.pem").read()
# private_key = open("private.pem").read()

# #Clave pública sin asociar a ninguna privada
# public_key2 = open("public2.pem").read()

# print("======== Empieza el programa =============")
# encoded = jwt.encode({"usuario": "Felipe Rodríguez", "rol": "profesor", "acceso": "administrador"}, private_key, algorithm="RS256")
# print(encoded)
# print("================================")
# decode = jwt.decode(encoded, public_key,algorithms="RS256", options={"verify_signature": True})
# print(decode)
# print("================================")
# #Forzamos fallo con la verificación de clave pública incorrecta

encoded = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzTm9ybWFsIiwiaWF0IjoxNjY3OTMzNTMzfQ.gfhw0dDxp6oixMLXXRP97W4TDTrv0y7B5YjD0U8ixrE"
encoded_hacker = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgcGFsb3RlcyIsInJvbCI6ImlzQWRtaW4iLCJpYXQiOjE2Njc5MzM1MzN9.krgBkzCBQ5WZ8JnZHuRvmnAZdg4ZMeRNv2CIAODlHRI"
clave = "Con KeepCoding aprendemos"
decode2 = jwt.decode(encoded_hacker, clave,algorithms="HS256", options={"verify_signature": True})
print(decode2)
print("======= Finaliza el programa =================")

