"""
Proyecto: Juego 'Adivina el Número'
Descripción:
El programa genera un número aleatorio y el usuario debe adivinarlo.
Incluye:
- Uso de funciones
- Bucles
- Condicionales
- Manejo de intentos
- Modularidad básica

Ideal para empezar con lógica de juegos en Python.
"""

import random

# Función para generar número secreto
def generar_numero(minimo, maximo):
    return random.randint(minimo, maximo)

# Función principal del juego
def jugar():
    print("=== Adivina el Número ===")

    minimo = 1
    maximo = 100
    numero_secreto = generar_numero(minimo, maximo)

    intentos = 0
    max_intentos = 10

    print(f"Estoy pensando un número entre {minimo} y {maximo}...")

    while intentos < max_intentos:
        try:
            intento = int(input("Tu intento: "))
        except ValueError:
            print("Por favor ingresá un número válido.")
            continue

        intentos += 1

        # Lógica de comparación
        if intento < numero_secreto:
            print("Muy bajo 📉")
        elif intento > numero_secreto:
            print("Muy alto 📈")
        else:
            print(f"¡Correcto! 🎉 Lo adivinaste en {intentos} intentos.")
            return

        print(f"Intentos restantes: {max_intentos - intentos}")

    print(f"Perdiste 😢 El número era: {numero_secreto}")


# Punto de entrada
if __name__ == "__main__":
    jugar()
