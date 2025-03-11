class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

    def pintar(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")