dicionario = {"banana": "fruta","casa":"imovel"}
print(dicionario)

valores_emitidos = all(valor for valor in dicionario.values())

if valores_emitidos:
    print("True")
else: 
    print("False")