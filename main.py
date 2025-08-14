def ejercicio1():
   acumulador=0
   list1=[1,2,3,4,5,6,7,8,9]
   for x in range (0, len(list1)):
       acumulador+=list1[x]
   print(acumulador)
def ejercicio2():
   texto=("programacion en python")
   contador=0
   for letra in texto:
       if letra in "AEIOUaeiou":
           contador+=1
   print(contador)
def ejercicio3():
    num=int(input("ingrese un numero:"))
    for x in range(1,11):
        multiplicacion=num*x
        print(multiplicacion)
def ejercicio4():
    lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num_pares = []
    for x in range(1, len(lista_num) + 1):
        if (x % 2) == 0:
            num_pares.append(x)
    print(num_pares)
    return num_pares
def ejercicio5():
    numero_filas = int(input("Proporciona el número de filas: "))
    for fila in range(1, numero_filas + 1):
        espacios_blanco = " " * (numero_filas - fila)
        asteriscos = "*" * (fila - 1)
        print(f"{asteriscos}{espacios_blanco}")
    for fila in range(1, numero_filas + 1):
        espacios_blanco = " " * (numero_filas - fila)
        asteriscos = "*" * (2 * fila - 1)
        print(f"{espacios_blanco}{asteriscos}")
    for fila in range(1, numero_filas + 1):
        espacios_blanco = " " * (numero_filas - fila)
        asteriscos = "*" * (fila - 1)
        print(f"{espacios_blanco}{asteriscos}")
