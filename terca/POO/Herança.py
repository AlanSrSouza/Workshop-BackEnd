class FormaGeometrica:
    def calculo(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, b, h):
        self.base = b
        self.altura = h

    def area(self):
        return self.base * self.altura

class Circulo(FormaGeometrica):
    PI = 3.14159 

    def __init__(self, r):
        self.raio = r

    def desenha(self):
        pass

    def area(self):
        return Circulo.PI * (self.raio ** 2)


retangulo = Retangulo(5, 3)
circulo = Circulo(9)
print("Área do Retângulo:", retangulo.area())
print("Área do Circulo:", circulo.area())