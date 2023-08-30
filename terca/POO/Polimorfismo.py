class Animal:
    def __init__(self):
        pass
    
    def barulho(self):
        pass

class Cachorro(Animal):
    def barulho(self):
        while True:
            escolha = input("O cachorro está com fome ou querendo chorar? (fome/chorar/sair): ")
            if escolha == "chorar":
                print("pipipipipipipi")
            elif escolha == "fome":
                print("AUUUUUUUUUUUUU")
            elif escolha == "sair":
                break
            else:
                print("Escolha inválida. Por favor, escolha 'fome', 'chorar' ou 'sair'.")

class Gato(Animal):
    def barulho(self):
        print(" O GATO DISE MIAAAAAAAAAAAAAU")

cachorro = Cachorro()
gato = Gato()

cachorro.barulho()
gato.barulho()
