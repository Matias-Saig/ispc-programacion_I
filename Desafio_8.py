"""
8- 
Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
$50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
del producto, el programa debe entregar las monedas de vuelto, una por una.

Producto A 270
Producto B 340
Producto C 390

Monedas
    10
    50
    100

Selección de producto
ingresar dinero
vuelto

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
