from Crypto.Util.Padding import pad, unpad
import base64
# Función para aplicar padding x923
def pad_x923(data, block_size):
    padding_len = block_size - len(data) % block_size
    padding = bytes([0] * (padding_len - 1) + [padding_len])
    return data + padding

# Función para eliminar padding x923
def unpad_x923(padded_data, block_size):
    padding_len = padded_data[-1]
    if padding_len > block_size or padding_len == 0:
        raise ValueError("Invalid padding")
    for byte in padded_data[-padding_len:-1]:
        if byte != 0:
            raise ValueError("Invalid padding")
    return padded_data[:-padding_len]

# Datos de ejemplo
data = base64.b64decode("TQ9SOMKc6aFS9SlxhfK9wT18UXpPCd505Xf5J/5nLI7Of/o0QKIWXg3nu1RRz4QWElezdrLAD5LO4USt3aB/i50nvvJbBiG+le1ZhpR84oI=")

# Tamaño del bloque (AES utiliza un tamaño de bloque de 16 bytes)
block_size = 16

# Aplicar padding PKCS7
padded_pkcs7 = pad(data, block_size, style='pkcs7')
print(f'Datos con padding PKCS7: {padded_pkcs7}')

# Aplicar padding x923
padded_x923 = pad_x923(data, block_size)
print(f'Datos con padding x923: {padded_x923}')

# Eliminar padding PKCS7
unpadded_pkcs7 = unpad(padded_pkcs7, block_size, style='pkcs7')
print(f'Datos sin padding PKCS7: {unpadded_pkcs7}')

# Eliminar padding x923
unpadded_x923 = unpad_x923(padded_x923, block_size)
print(f'Datos sin padding x923: {unpadded_x923}')
