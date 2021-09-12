def conversor(tipo_pesos, valor_dolar):
    pesos = input("Ingrese el valor en" + tipo_pesos + ": ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares +  " dólares")

menu = """
Bienvenid@ al conversor de monedas 💰

1 - COP (Pesos COlombianos) a USD
2 - ARS (Pesos Argentinos) a USD
3 - MXN (Pesos Mexicanos) a USD
4 - USD a COP

Elige una opción: """

opcion = input(menu)

if opcion == "1":
    conversor('COP', 3835)

elif opcion == "2":
    conversor('ARS', 65)

elif opcion == "3":
    conversor('MXN', 24)

elif opcion == "4":
    conversor('USD', 1/3835)

else:
    print("Value Error")
    input("¿Qué opción quieres 1 o 2?: ")