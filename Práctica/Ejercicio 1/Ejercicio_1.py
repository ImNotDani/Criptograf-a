#XOR de datos binarios
def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])


kfija = bytes.fromhex("B1EF2ACFE2BAEEFF")
kfinal = bytes.fromhex("91BA13BA21AABB12")

print("La clave en properties es: ",xor_data(kfija,kfinal).hex())


#Parte 2 ejercicio 1 practica

kfija2 = bytes.fromhex("B1EF2ACFE2BAEEFF")
kprop = bytes.fromhex("B98A15BA31AEBB3F")

print("La clave final es: ",xor_data(kfija2,kprop).hex())


