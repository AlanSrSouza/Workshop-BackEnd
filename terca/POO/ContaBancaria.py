class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.saldo -= valor
        else:
            print(f'O valor de {valor} excede o saldo disponível para saque')
    def __pode_sacar(self, valor):
        return valor <= self.saldo
    
    def get_saldo(self):
        return f'O {self.titular} tem o saldo de {self.saldo}'

cliente = ContaBancaria('Pedro', 1000)
cliente.depositar(500)  # Depositar 500
cliente.sacar(300)      # Sacar 300

saldo_atual = cliente.get_saldo()  # Verificar o saldo restante
print(f'O saldo atual de {cliente.titular} é {saldo_atual}')
