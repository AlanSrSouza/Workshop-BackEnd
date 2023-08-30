class Pessoa(): 
    def __init__(self, nome, idade, professor):
        self.nome = nome
        self.idade = idade
        self.professor = professor

    def saudacao(self):
     return f'oi, meu nome é {self.nome}, tenho {self.idade} anos e sou {self.professor}'
        
pedro = Pessoa('Pedro', 28, 'Dev')
mensagem = pedro.saudacao()
print(mensagem)
