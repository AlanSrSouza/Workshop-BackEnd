def contagem_de_sexos(F, M):
    while True:
        sexo = input("Informe o sexo com F(Feminino) ou M(Masculino), ou digite 'sair' para encerrar o programa: ")

        if sexo == "sair":
            break

        if sexo == "F":
            F += 1
        elif sexo == "M":
            M += 1
        else:
            print("Sexo inválido.")

    print("Quantidade de femininos: {}\nQuantidade de Masculinos: {}".format(F, M))


contagem_F = 0
contagem_M = 0


contagem_de_sexos(contagem_F, contagem_M)
