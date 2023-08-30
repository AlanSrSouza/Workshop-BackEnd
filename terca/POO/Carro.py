class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        return f"Seu carro {self.marca} de modelo {self.modelo} e ano {self.ano}"

    def velocidade(self):
        velocidade = 0
        while True:
           velocidade= int(input(" Digite a velocidade do Carro:"))
           if velocidade > 100:
                input("Você está prestes a decolar")
           else:
                input ("Você é o cara")


cliente = Carro('Chevrolé', 'compacto', 2018)
print(cliente.acelerar())
cliente.velocidade()

