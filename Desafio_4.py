"""
4- Tiempo de viaje. Un viajero desea saber cuánto tiempo tomó un viaje que realizó. Él
tiene la duración en minutos de cada uno de los tramos del viaje.

Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado el tiempo total de viaje en formato horas:minutos.
El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

Duración tramo: 15
Duración tramo: 30
Duración tramo: 87
Duración tramo: 0
Tiempo total de viaje: 2:12 horas 
"""


def query_ctrl(msg):
    while True:
        try:
            time = int(input(msg))
            if time >= 0:
                return time
            elif time < 0:
                print(
                    f'No se pueden ingresar números negativos. Ingrese un valor valido\n')

        except ValueError:
            print('El valor no es válido. Ingrese los minutos de su tramo (ejemplo 45): ')


print('Tiempo de viaje')

acc = 0
acc_minutes = 0
while True:
    query_minutes = query_ctrl(
        '\nCuántos minutos son este tramo? (0 para terminar) ')

    if query_minutes == 0:
        hours = acc_minutes // 60
        minutes = acc_minutes % 60
        days = round((acc_minutes / 1440), 1)
        print(
            f'\nTiempo total del viaje: \n  {acc_minutes} minutos ~ {hours}:{minutes:02} hs, {days} días')
        break

    acc += 1
    acc_minutes += query_minutes
    print(f'Tramo {acc}: {query_minutes} minutos\n')
