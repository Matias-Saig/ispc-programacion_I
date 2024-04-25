# 2- Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

def query_ctrl(msg, min_time, max_time):
    while True:
        try:
            time = int(input(msg))
            if time >= min_time and time <= max_time:
                return time
            elif time > max_time:
                print(
                    f'Ingresaste {time} hs, el valor máximo es de {max_time} hs. Ingrese un valor valido')
            else:
                print(
                    f'Ingresaste {time} hs, el valor minimo es de {min_time} hs. Ingrese un valor valido')

        except ValueError:
            print('Ingrese un número entero.')


print('Que hora es? ')
query_hour = query_ctrl('  hora (24hs): ', 0, 24)
query_minutes = query_ctrl('  minutos: ', 0, 60)

print(f'Hora actual: {query_hour}:{query_minutes} hs\n')

query_next_hour = query_ctrl(
    f'Quieres saber que hora será cuando pasen algunas horas? \n  Cuantas horas quieres agregar?: ', 0, 99999)
query_next_minutes = query_ctrl(
    f'  Cuantos minutos quieres agregar?: ', 0, 99999)

next_hour = (query_hour + query_next_hour) % 24
next_minutes = (query_minutes + query_next_minutes) % 60
next_day = (query_hour + query_next_hour) // 24

print(f'\nDentro de {query_next_hour} hs y {query_next_minutes} minutos, serán las {next_hour}:{next_minutes:02} hs, dentro de {next_day} días.\n')
