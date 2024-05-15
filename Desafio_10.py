"""
10- Torre y Alfil. Un tablero de ajedrez es una grilla de ocho filas y ocho columnas,
numeradas de 1 a 8. Dos de las piezas del juego de ajedrez son el alfil y la torre. El alfil se
desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una
pieza puede ser capturada por otra si está en una casilla a la cual la otra puede
desplazarse:
Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de
una torre, e indique cuál pieza captura a la otra:
"""


# control pregunta
def query_ctrl(msg):
    error = "    No es válido. Puede ingresar del 1 al 8"
    while True:
        try:
            control = int(input(msg))
            if 0 < control <= 8:
                return control
            else:
                print(error)

        except ValueError:
            print(error)

# pregunta, posición de pieza
def chess_piece_ctrl(title):
    print(f"\n{title}")
    row_control = query_ctrl("  Fila: ")
    column_control = query_ctrl("  Columna: ")
    return [row_control, column_control]


# TORRE
def tower_attack(tower_pos, bishop_pos):
    # row
    if tower_pos[0] == bishop_pos[0]:
        return [True, bishop_pos[0], bishop_pos[1], "horizontal"]
    # column
    if tower_pos[1] == bishop_pos[1]:
        return [True, bishop_pos[0], bishop_pos[1], "vertical"]
    return [False]


# ALFIL
# movimiento
def bishop_move(bishop_pos, tower_pos, row_change, column_change):
    bishop_row, bishop_column = bishop_pos

    while (row[0] <= bishop_row <= row[-1]) and (column[0] <= bishop_column <= column[-1]):

        if bishop_row == tower_pos[0] and bishop_column == tower_pos[1]:
            return True
        else:
            bishop_row += row_change
            bishop_column += column_change
    return False

# ataque
def bishop_attack(bishop_pos, tower_pos):
    condicional = [True, bishop_pos[0], bishop_pos[1]]

    if bishop_move(bishop_pos, tower_pos, 1, -1):
        condicional.append("frontal izquierdo")
        return condicional

    if bishop_move(bishop_pos, tower_pos, 1, 1):
        condicional.append("frontal derecho")
        return condicional

    if bishop_move(bishop_pos, tower_pos, -1, -1):
        condicional.append("descendente izquierdo")
        return condicional

    if bishop_move(bishop_pos, tower_pos, -1, 1):
        condicional.append("descendente derecho")
        return condicional

    return [False]


# Movimientos
def chess_move(bishop, tower):

    print(f"""
Alfil: fila {bishop[0]}  columna {bishop[1]}
Torre: fila {tower[0]}  columna {tower[1]}
""")
    tower_result = tower_attack(tower, bishop)
    bishop_result = bishop_attack(bishop, tower)

    if tower_result[0]:
        print(
            f"\n# Torre captura Alfil, en ataque {tower_result[3]} en fila {tower_result[1]} y columna {tower_result[2]}")
    elif bishop_result[0]:
        print(
            f"\n# Alfil captura Torre, en ataque {bishop_result[3]} en fila {bishop_result[1]} y columna {bishop_result[2]}")
    else:
        print("\n# Ninguna captura")


# Tablero
row = [1, 2, 3, 4, 5, 6, 7, 8]
column = [1, 2, 3, 4, 5, 6, 7, 8]

# Ejecución
print("\nTorre vs Alfil")
print("(Las filas y columnas están enumeradas del 1 al 8)")

bishop_position = chess_piece_ctrl("Cuál es la posición del Alfil")
tower_position = chess_piece_ctrl("Cuál es la posición de la Torre")

chess_move(bishop_position, tower_position)
