# 1- Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:
msg = f"Ingrese un número de tres cifras: "

while True:
  numbers = input(msg)

  if numbers.isdecimal() and len(numbers) == 3:
    break 

  if numbers.isalpha():
    print(f'"{numbers}" es una palabra\n')
  elif len(numbers) > 3:
    print(f'El número {numbers} tiene más cifras\n')
  else:
    print(f'El número {numbers} tiene menos cifras\n')

print(f'El número en orden inverso es: {numbers[::-1]}')