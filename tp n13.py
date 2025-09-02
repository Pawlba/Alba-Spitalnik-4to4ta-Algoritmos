def ejercicio1():
   matriz=[[1,2,3],
           [4,5,6],
           [7,8,9]]
   for x in range(0, len(matriz)):
       print(matriz[x])
def ejercicio2():
   matriz = [[10, 20, 30],
             [40, 50, 60],
             [70, 80, 90]]
   suma = 0
   for x in range(0, len(matriz)):
       for y in range(0, len(matriz[x])):
           suma += matriz[x][y]
   print(suma)
def ejercicio3():
   matriz=[[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [1,7,4,9]]
   indice_c=int(input("ingrese un indice de columnas:"))
   indice_f=int(input("ingrese un indice de filas:"))
   print(matriz[indice_f][indice_c])
def ejercicio4():
   matriz = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [1, 7, 4, 9]]


   maximo = [0][0]


   for fila in matriz:
       for num in fila:
           if num > maximo:
               maximo = num


   print(f"el numero mayor es: {maximo}")
