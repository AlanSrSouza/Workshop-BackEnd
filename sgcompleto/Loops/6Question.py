#SEXTA QUESTÂO

total = 0

while True:
    num = int(input("Digite um número diferente de 0 (ou 0 para sair): "))
    
    if num == 0:
        break
    
    total += num


print("A soma dos números digitados é:", total)