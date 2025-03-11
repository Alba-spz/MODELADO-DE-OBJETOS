from Persona import Persona

class Windsor(Persona):
    def __init__(self, nombre):
        super().__init__(nombre, "Windsor")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
        