from Figura import Figura

class Elipse(Figura):
    def __init__(self, eje_mayor, eje_menor):
        super().__init__("Elipse")
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

    def pintar(self):
        print(f"Pintando una {self.nombre} con eje mayor {self.eje_mayor} y eje menor {self.eje_menor}")