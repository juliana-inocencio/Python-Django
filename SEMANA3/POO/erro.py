def calcular_media(valores):
    soma = 0.0
    for valor in valores:
        soma += valor
    tamanho = len(valores)  
    media = soma / tamanho if tamanho > 0 else 0 
    return media

continuar = True 
valores = []

while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        continuar = False
    else:
        valores.append(float(valor))  

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {:.2f}'.format(valores, media))

