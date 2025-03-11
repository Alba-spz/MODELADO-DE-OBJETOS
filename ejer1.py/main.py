from Circulo import Circulo
from Cuadrado import Cuadrado
from Elipse import Elipse

def main():
    figuras = [
        Circulo(5),
        Cuadrado(4),
        Elipse(4, 6)
    ]

    for figura in figuras:
        figura.pintar()

if __name__ == "__main__":
    main()