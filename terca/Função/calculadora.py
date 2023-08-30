def calculadora():
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mult(a, b):
        return a * b

    def div(a, b):
        if b != 0:
            return a / b
        else:
            return "Divisão por zero não é permitida"

    var = input('Digite a operação desejada: ')
    numero = int(input('Digite um número: '))
    numero2 = int(input('Digite outro número: '))

    if var == 'soma':
        resultado = soma(numero, numero2)
    elif var == 'subtracao':
        resultado = sub(numero, numero2)
    elif var == 'multiplicacao':
        resultado = mult(numero, numero2)
    elif var == 'divisao':
        resultado = div(numero, numero2)
    else:
        resultado = 'Operação não reconhecida'

    print("Resultado:", resultado)

calculadora()
