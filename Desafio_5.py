"""
    5- Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido
    exactamente 365 rotaciones sobre sí misma, sino un poco más. Más precisamente, la
    diferencia es de más o menos un cuarto de día.
    Para evitar que las estaciones se desfasen con el calendario, el calendario juliano
    introdujo la regla de introducir un día adicional en los años divisibles por 4 (llamados
    bisiestos), para tomar en consideración los cuatro cuartos de día acumulados.
    Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente
    3/400 de día.
    Para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo
    calendario, en el que el último año de cada siglo dejaba de ser bisiesto, a no ser que
    fuera divisible por 400.
    Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era
    el calendario vigente en ese año
"""


# función de control
def query_ctrl(msg):
    while True:
        try:
            time = int(input(msg))

            if (time != 0) and (time > -45):
                return time
            elif time == 0:
                print('En el calendario juliano no hay año 0.\n')
            elif time < -45:
                print(
                    'Los bisiestos se cuentan a partir del año -45 A.C., no se incluyen los anteriores\n')

        except ValueError:
            print('El valor no es válido. Ingrese el año a evaluar (ejemplo 150 o -44): ')


# Inicio
print("""
      Años bisiestos
      Calendario juliano: -45 a 1581; Calendario gregoriano: 1582 en adelante
      (Ingresar 9999 para finalizar)""")


while True:
    cal_greg = "calendario gregoriano -"
    cal_jul = "calendario juliano -"

    # Pregunta
    year = query_ctrl("\nIngrese el año a evaluar: ")

    # Finalización
    if year == 9999:
        break

    # Evaluación según calendario juliano
    if year >= -45 and year <= 1581:
        if year % 4 == 0:
            print(f"{cal_jul} {year} es un año bisiesto")
        else:
            print(f"{cal_jul} {year} NO es un año bisiesto")

    # Evaluación según calendario gregoriano
    elif year >= 1582:
        if year % 4 == 0 and not year % 100 == 0:
            print(f"{cal_greg} {year} es un año bisiesto")
        elif year % 4 == 0 and year % 400 == 0:
            print(f"{cal_greg} {year} es un año bisiesto")
        else:
            print(f"{year} NO es un año bisiesto {cal_greg}")
