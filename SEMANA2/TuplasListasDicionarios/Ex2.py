nome = input("Digite seu nome: ")

letras = []
for i in range(len(nome)-1,-1,-1):
    letras.append(nome[i].upper())

print("".join(letras))