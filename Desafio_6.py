""" 
    6- Escribir un programa que pida al usuario un número entero y muestre por pantalla un
    triángulo rectángulo como el de más abajo con tantos renglones como indique el
    usuario.
    Ingrese cantidad de renglones: 5
    2
    4 2
    6 4 2
    8 6 4 2
    10 8 6 4 2 
"""

# función de control


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


print("Triángulo rectángulo")
while True:
    # Pregunta
    lines = query_ctrl("Cuantos reglones quieres hacer? (0 para salir): ",
                       "Ingrese un número entero, por favor\n")
    # Salida
    if lines == 0:
        print()
        break
    
    # Triángulo
    for row in range(1, lines + 1):
        for column in range(1, row + 1):
            print(column*2, end=" ")
        print()
