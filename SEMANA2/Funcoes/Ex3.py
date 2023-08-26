def fahrenheitCelsius(grausF):
    return(grausF - 32) * 5/9

def menu():
    print("Escolha uma opção: ")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")
    escolhido = input("Digite o npumero da opção desejada: ")
    return escolhido

escolhido = menu()

if escolhido == "1":
    grausC = float(input("Digite a temperatura em graus Celsius:"))
    fahrenheit = celsiusFahrenheit(grausC)
    print(f"Valor em Fahrenheit: {fahrenheit} °F")
elif escolhido == "2":
    grausF = float(input("Digite a temperatura em graus Fahrenheit:"))
    celsius = fahrenheitCelsius(grausF)
    print(f"Valor em Celsius: {celsius} °F")
else:
    print("Opção inválida")