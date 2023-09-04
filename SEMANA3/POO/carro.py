class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.cor} {self.modelo} foi ligado.")
        else:
            print("O carro já está ligado.")

    def desliga(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print(f"O carro {self.cor} {self.modelo} foi desligado.")
        else:
            print("O carro já está desligado.")

    def acelera(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"O carro {self.cor} {self.modelo} acelerou para {self.velocidade} km/h.")
        else:
            print("O carro está desligado. Ligue-o primeiro.")

    def desacelera(self, decremento):
        if self.ligado:
            if self.velocidade >= decremento:
                self.velocidade -= decremento
                print(f"O carro {self.cor} {self.modelo} desacelerou para {self.velocidade} km/h.")
            else:
                print("O carro já está parado.")
        else:
            print("O carro está desligado. Ligue-o primeiro.")

# Criando uma instância da classe Carro
meu_carro = Carro(cor="Azul", modelo="Sedan")

# Testando os métodos da classe
meu_carro.liga()
meu_carro.acelera(30)
meu_carro.desacelera(10)
meu_carro.desliga()
