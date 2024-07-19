from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256

import os
my_path = os.path.abspath(os.getcwd())

fichero_pub = "C:\\Users\\dmore\\Desktop\\Ciberseguridad\\Criptografia\\Hashing\\clave-rsa-oaep-publ.pem"
f=open(fichero_pub,'r')
keypub= RSA.import_key(f.read())




mensaje = bytes.fromhex("e2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72")

encryptor = PKCS1_OAEP.new(keypub,SHA256)
encrypted = encryptor.encrypt(mensaje)

print("Cifrado:", encrypted.hex())
print("--------------------------------------------------")

#dc767708508c68b9106fc6b9b39ff2a225e7ce0ab8b7795f706e473d9bdd4933c7fd5c7e378dfb615f2c18d142e422693d573f6cd693fa42940af019b3565cddac07ee0fa811981ac852e31b8c40a50b77fa46e04095f54f73172e54422123886526520cba25ea35c62a29e3950245f9fadc61dc1364012c3ff29110afa07adddebef5d6c12e20719e2664dd277e1dc090f65e6c9c3c786659acb4b8c55ff70360ed6946d6319474578eddcb7c127cb701978050ac108de7b18ce5f59d99d0c92da63a4df90d5760257530182c770a70c6e74d752ecd847313d7002238db009353fee0ce761b8356fe4263c4a7e6fa254885470a8fbac97a34fa4de36421135f