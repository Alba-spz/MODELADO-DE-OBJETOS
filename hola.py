import math

class Figura:
    def area(self):
        pass

    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

class Elipse(Figura):
    def __init__(self, eje_mayor, eje_menor):
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

    def area(self):
        return math.pi * self.eje_mayor * self.eje_menor

    def perimetro(self):
        # Aproximación de Ramanujan
        h = ((self.eje_mayor - self.eje_menor) ** 2) / ((self.eje_mayor + self.eje_menor) ** 2)
        return math.pi * (self.eje_mayor + self.eje_menor) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho

    def perimetro(self):
        return 2 * (self.largo + self.ancho)