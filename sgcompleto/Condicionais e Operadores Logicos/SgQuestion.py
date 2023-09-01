velocidade = int(input("Velocidade registrada pelo radar: "))
if (velocidade > 80):
    print("Sua velocidade atingida foi ", velocidade,
          f"km/h você foi multado em {(velocidade-80)*7}")
else:
    print("suave")

