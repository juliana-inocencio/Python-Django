print("Digite o turno que você estuda: ")
print("M - Matutino")
print("V - Vespertino")
print("N - Noturno")
turno = str(input(""))

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Opção inválida!")