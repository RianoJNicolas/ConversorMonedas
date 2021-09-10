menu = """
Bienvenid@ al conversor de monedas 💰

1 - COP (Pesos COlombianos) a USD
2 - ARS (Pesos Argentinos) a USD
3 - MXN (Pesos Mexicanos) a USD
4 - USD a COP

Elige una opción: """

opcion = input(menu)

if opcion == "1":
    pesos = input("Ingrese el valor en COP: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares +  " dólares")

elif opcion == "2":
    pesos = input("Ingrese el valor en ARS: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares +  " dólares")

elif opcion == "3":
    pesos = input("Ingrese el valor en MXN: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares +  " dólares")

elif opcion == "4":
    dolares = input("Ingrese el valor en USD: ")
    dolares = float(dolares)
    valor_dolar = 3875
    pesos = dolares * valor_dolar
    pesos = round(pesos, 2)
    pesos = str(pesos) 
    print("Tienes $" + pesos +  " Pesos")

else:
    print("Value Error")
    input("¿Qué opción quieres 1 o 2?: ")