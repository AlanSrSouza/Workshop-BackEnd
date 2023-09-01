#SÉTIMA QUESTÃO
F = 0
M = 0

while True:
    sexo = input("Informe o sexo como F (feminino) ou M (masculino), ou digite 'sair' para encerrar: ")

    if sexo == "sair":
        break
    
    if sexo == "F":
        F += 1
    elif sexo == "M":
        M += 1
    else:
        print("Sexo inválido. Digite 'F' para feminino, 'M' para masculino.")

print("Quantidade de femininos: {}, \nQuantidade de masculinos: {}".format(F, M))