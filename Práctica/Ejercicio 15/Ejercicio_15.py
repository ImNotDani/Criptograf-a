from psec import tr31


def importar():
    kbpk_b = bytes.fromhex("A1A10101010101010101010101010102")
    kb = "D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B"
    MykeyBlock =tr31.KeyBlock(kbpk_b).unwrap(kb).hex()
    print("Importar Clave:" + tr31.KeyBlock(kbpk_b).unwrap(kb).hex())
    print("Mode use:" + tr31.KeyBlock(MykeyBlock).header.mode_of_use)
   # print("Header: "+ str(MykeyBlock.header))


# def exportar():
#     h = tr31.Header()
#     h.version_id = "D"
#     h.key_usage = "D0"
#     h.algorithm = "A"
#     h.mode_of_use = "B"
#     h.exportability = "S"

#     #Esta es la clave con la que cifro la otra clave. Key Encryption Key (KEK)
#     kbpk = bytes.fromhex("A1A10101010101010101010101010103")

#     # Esta es la clave que queremos exportar.
#     key = bytes.fromhex("D2D1c1c1c1c1c1c1c1c1c1c1c1c1c1F2")
#     kb = tr31.KeyBlock(kbpk, h)
#     print("Fase de Exportación del bloque de clave TR31: " + kb.wrap(key))


if __name__ == "__main__":
    # exportar()
    importar()
    #exportar()
