from Persona import Persona

class Spencer(Persona):
    def __init__(self, nombre):
        super().__init__(nombre, "Spencer")
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
        