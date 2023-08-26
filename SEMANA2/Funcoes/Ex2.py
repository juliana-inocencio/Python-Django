def reverte (numero):
    numero_str = str(numero)
    reverso = []

    for n in range(len(numero_str)-1,-1,-1):
        reverso.append(numero_str[n])

    reverso = int(''.join(reverso))
    return reverso

num = int(input('Digite um número: '))
print(
    reverte(num)
)