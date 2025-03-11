from Persona import Persona
class Middleton(Persona):
    def __init__(self, nombre):
        super().__init__(nombre, "Middleton")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
        