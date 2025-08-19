def ejercicio1():
    num1=int(input("inserte un numero"))
    num2=int(input("inserte otro numero"))
    try:
        result = num1 / num2
        print(result)
    except ZeroDivisionError:
        print("Error: No puedes dividir por cero.")
def ejercicio2():
    try:
        Age = int(input("ingrese su edad"))
        print(f"su edad es {Age}")
    except ValueError:
        print("caracter incorrecto, ingrese de nuevo su edad.")
def ejercicio3():
    nombres = ["Ana", "Pedro", "Sofía"]
    try:
        Indice=int(input("ingrese un indice:"))
        print(nombres[Indice])
    except IndexError:
        print("su numero excede el indice de la lista")
def ejercicio4():
    try:
        num1 = int(input("inserte un numero"))
        num2 = int(input("inserte otro numero"))
        result = num1 + num2
        print(result)
    except ValueError:
        print("Error: No puedes dividir.")
def ejercicio5():
    try:
        num1 = int(input("inserte un numero"))
        num2 = int(input("inserte otro numero"))
        division= num1/num2
        print(division)
    except ZeroDivisionError:
        print("no se divide por cero")
    except ValueError:
        print("ingrese numeros enteros muy balatreros")
    finally:
        print("idk")