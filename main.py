import os
import subprocess

def run_exercise(exercise_number):
    if exercise_number == 1:
        subprocess.run(["python", "Ejercicio1/main.py"])
    elif exercise_number == 2:
        subprocess.run(["python", "Ejercicio2/main.py"])
    elif exercise_number == 3:
        subprocess.run(["python", "Ejercicio3/main.py"])
    else:
        print("Número de ejercicio no válido.")

def main():
    while True:
        print("Menú de Ejercicios")
        print("1. Ejecutar Ejercicio 1")
        print("2. Ejecutar Ejercicio 2")
        print("3. Ejecutar Ejercicio 3")
        print("4. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            run_exercise(1)
        elif choice == '2':
            run_exercise(2)
        elif choice == '3':
            run_exercise(2)
        elif choice == '4':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()