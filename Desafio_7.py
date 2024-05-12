"""
7- secuencia de Collatz 
"""

# control
def query_ctrl(msg, error):
    while True:
        try:
            control = int(input(msg))
            if control >= 0:
                return control
            else:
                print("El número debe ser positivo")

        except ValueError:
            print(error)


# Secuencia de Collatz
def collatz(n):
    while True:
        print(n, end=" ")

        # Salida
        if n == 1:
            print()
            break

        # Calculo
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1


print("Secuencia de Collatz")

while True:
    # Pregunta
    number = query_ctrl("Ingrese un número entero? (0 para salir): ",
                        "Ingrese un número entero positivo, por favor\n")

    # Salida
    if number == 0:
        print()
        break

    # Función
    collatz(number)
