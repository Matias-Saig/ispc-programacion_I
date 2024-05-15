"""
10- Torre y Alfil. Un tablero de ajedrez es una grilla de ocho filas y ocho columnas,
numeradas de 1 a 8. Dos de las piezas del juego de ajedrez son el alfil y la torre. El alfil se
desplaza en diagonal, mientras que la torre se desplaza horizontal o verticalmente. Una
pieza puede ser capturada por otra si está en una casilla a la cual la otra puede
desplazarse:
Escriba un programa que reciba como entrada las posiciones en el tablero de un alfil y de
una torre, e indique cuál pieza captura a la otra:


Fila alfil: 7
Columna alfil: 6
Fila torre: 4
Columna torre: 3
Alfil captura

Fila alfil: 3
Columna alfil: 4
Fila torre: 7
Columna torre: 4
Torre captura

Fila alfil: 3
Columna alfil: 3
Fila torre: 8
Columna torre: 5
Ninguna captura


 """

# TORRE
def tower_attack(tower_pos, bishop_pos):
    print("- Ataque de Torre -")
    # row
    if tower_pos[0] == bishop_pos[0]:
        return [True, bishop_pos[0], bishop_pos[1], "horizontal"]
    #column
    if tower_pos[1] == bishop_pos[1]:
        return [True, bishop_pos[0], bishop_pos[1], "vertical"]
    print("Torre no puede atacar Alfil")
    return False
    

# ALFIL
# ataque ascendente
def bishop_attack_forward(bishop_pos, tower_pos):
    bishop_row, bishop_column = bishop_pos
   
    while bishop_row < row[-1] and bishop_column < column[-1]:             
        if bishop_row == tower_pos[0] and bishop_column == tower_pos[1]:
            return [True, bishop_row, bishop_column]
        else:
            bishop_row += 1 
            bishop_column += 1

# ataque descendente
def bishop_attack_backward(bishop_pos, tower_pos):
    bishop_row, bishop_column = bishop_pos
    
    while bishop_row > row[0] and bishop_column > column[0]:             
        if bishop_row == tower_pos[0] and bishop_column == tower_pos[1]:
            return [True, bishop_row, bishop_column]
        else:
            bishop_row -= 1 
            bishop_column -= 1

# ataque 
def bishop_attack(bishop_pos, tower_pos):
    print("\n- Ataque de Alfil -")
        
    forward = bishop_attack_forward(bishop_pos, tower_pos)
    backward = bishop_attack_backward(bishop_pos, tower_pos)
        
    if not forward == None and forward[0] == True:
        return print(f"\nAlfil captura a torre en ataque ascendente en fila {forward[1]} y columna {forward[2]}")
    
    if not backward == None and backward[0] == True:
        return print(f"\nAlfil captura a torre en ataque descendente en fila {backward[1]} y columna {backward[2]}")
     
    print("- Alfil no puede capturar a torre -")
    return False 

def chess_move(bishop, tower):
    tower_result = tower_attack(tower, bishop)
    bishop_result = bishop_attack(bishop, tower)

    if tower_result == True:
        print("\n# Torre gana")
    elif bishop_result == True:
        print("\n# Alfil gana")
    else:
        print("\n# Ninguna captura")



# Tablero
row = [1,2,3,4,5,6,7,8]
column = [1,2,3,4,5,6,7,8]

# position: [row, column]
bishop_position = [7,6] 
tower_position = [7,3]

# Ejecución
chess_move(bishop_position,tower_position)

        
# print(f"bishop: {bishop_pos} || tower: {tower_pos}")


    
            



