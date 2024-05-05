"""
    3- Escribir un programa que pida al usuario un número entero y muestre por pantalla si
    es un número primo o no. 
"""

# función de control
def query_ctrl(msg, error):
    while True:
        try:
            control = int(input(msg))
            if control > 0 and isinstance(control, int):
                return control
            else:
                print("El número debe ser positivo")

        except ValueError:
            print(error)

# función verificación de números primos
def isPrime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return i
    return True

# Pregunta: número
number = query_ctrl("Ingrese un número entero: ",
                    "\nNo es valido, ingrese otro número, ej. 1:")

# Evaluación de número
result = isPrime(number)
if result == True:
    print("\nEs un número primo")
else:
    print(f"\nNo es un número primo, porque es divisible por {result}")
