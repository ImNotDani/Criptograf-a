import hashlib


# initiating the "s" object to use the
# sha3_256 algorithm from the hashlib module.
s = hashlib.sha3_256()

# will output the name of the hashing algorithm currently in use.
print(s.name)

# will output the Digest-Size of the hashing algorithm being used.
print(s.digest_size)

# providing the input to the hashing algorithm.
s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía.","UTF-8"))


print("a) 64 carácteres hex = 256 bits (SHA3-256)")
print("b) 128 carácteres hex = 512 bits (SHA2-512)")
print("c)", s.hexdigest())
print("d) Destacaría la sensibilidad a cambios.")

