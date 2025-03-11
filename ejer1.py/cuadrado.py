from Figura import Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado

    def pintar(self):
        print(f"Pintando un {self.nombre} con lado {self.lado}")