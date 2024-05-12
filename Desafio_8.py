"""
8- 
Una máquina de alimentos tiene productos de tres tipos, A, B y C, que valen
respectivamente $270, $340 y $390. La máquina acepta y da de vuelto monedas de $10,
$50 y $100.
Escriba un programa que pida al usuario elegir el producto y luego le pida ingresar las
monedas hasta alcanzar el monto a pagar. Si el monto ingresado es mayor que el precio
del producto, el programa debe entregar las monedas de vuelto, una por una.

"""

# control ingreso producto
def query_products(msg, products):
    while True:
        control = input(msg).upper()    
        if control in products:
            return products[control]
        else:
            print("El producto ingresado no es correcto. Seleccione el producto A, B o C\n")


# control ingreso dinero
def query_ctrl_number(msg, error, coins):
    while True:
        try:
            control = int(input(msg))
            if control in coins:
                return control
            else:
                print(error, "\n")

        except ValueError:
            print(error, "\n")


# Ingresar dinero
def coin_add(n, product, coins):
    if n > 0:
        print(f"  Dinero ingresado: ${n}   Faltante: ${product - n}\n")

    add = query_ctrl_number("Cuánto quieres ingresar?: ",
                            "Solo puedes ingresar 10, 50 0 100", coins)
    
    for coin in coins:
        if coin == add:
            n += coin
    
    return n

# Vuelto de dinero
def money_back(n, product, coins):
    rest = n - product
    change = 0
    while rest > 0:
        for coin in coins:
            if rest >= coin:
                rest -= coin
                change += coin
                print(f"  ${coin}")
    return change


# Cálculo total
def total_amount(product, coins):
    print(f"El total a pagar es ${product} \n")
    print(f"Puedes ingresar {coins[2]}, {coins[1]} y {coins[0]} para pagar")

    money = 0
    while money < product:
        money = coin_add(money, product, coins)
    if money == product:
        print(
        f"Producto: ${product}    Total ingresado: ${money} \n- Producto pagado - \n")

    if money > product:
        print("\nSu vuelto:")
        change = money_back(money, product, coins)
        print(f"\nProducto: ${product}    Total ingresado: ${money}    Vuelto: ${change} \n- Producto pagado - \n")

# Ejecución
products = {"A": 270, "B": 340, "C": 390}

print("Productos disponibles:")
for opc, cost in products.items():
        print(f"    {opc}) ${cost}")

coins = (100, 50, 10)

selected = query_products(f"Seleccione un producto:", products)

total_amount(selected, coins)