from Windsor import Windsor
class Gales(Windsor):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.titulo = "de Gales"

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.titulo}"