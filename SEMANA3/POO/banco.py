from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal

    @abstractmethod
    def calcula_cheque_especial(self):
        pass

class ClienteMulher(Cliente):
    def calcula_cheque_especial(self):
        return self.renda_mensal

class ClienteHomem(Cliente):
    def calcula_cheque_especial(self):
        return 0

class ContaCorrente:
    def __init__(self, clientes=[]):
        self.saldo = 0
        self.operacoes = []
        self.clientes = clientes

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(f"Depósito: +{valor}")
        return f"Depósito de {valor} realizado com sucesso."

    def saque(self, valor):
        if self.saldo - valor >= -self.calcula_cheque_especial():
            self.saldo -= valor
            self.operacoes.append(f"Saque: -{valor}")
            return f"Saque de {valor} realizado com sucesso."
        else:
            return "Saldo insuficiente."

    def extrato(self):
        return f"Saldo: {self.saldo}\nOperações: {', '.join(self.operacoes)}"

    def calcula_cheque_especial(self):
        cheque_especial = 0
        for cliente in self.clientes:
            cheque_especial += cliente.calcula_cheque_especial()
        return cheque_especial

# Exemplo de uso:
cliente1 = ClienteMulher("Maria", "123456789", 5000)
cliente2 = ClienteHomem("João", "987654321", 6000)

conta = ContaCorrente([cliente1, cliente2])

print(conta.deposito(1000))
print(conta.saque(3000))
print(conta.extrato())
