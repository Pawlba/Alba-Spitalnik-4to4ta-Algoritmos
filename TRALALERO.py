def ejercicio_1():
   Matriz = [
       [1,2,3,4],
       [6,2,1,2],
       [1,3,2,4],
       [5,6,7,8]
   ]


   for x in range(len(Matriz)):
       aux = 0
       for y in range(len(Matriz[x])):
           aux += Matriz[x][y]
       print(aux)


   for j in range(len(Matriz[0])):
       aux = 0
       for k  in range(len(Matriz)):
           aux += Matriz[k][j]
       print(aux)


def ejercicio_2():
   Matriz = [
       [1,2,3,4],
       [6,2,1,2],
       [4,3,2,1],
       [5,6,7,8]
   ]


   Matriz2 = []
   for x in range(len(Matriz)-1,-1,-1):
       listaaux = []
       for y in range(len(Matriz[x])-1,-1,-1):
           listaaux.append(Matriz[x][y])
       Matriz2.append(listaaux)


   print(Matriz2)


def ejercicio_3():
   cont=0
   matriz=[
       [1, 5, 3, 5],
       [8, 5, 9, 2],
       [4, 5, 6, 7]
   ]
   num=int(input("ingrese un numero:"))
   for x in range(len(matriz)):
       for y in range(len(matriz[x])):
           if num == matriz[x][y]:
               cont+=1
   print(cont)
def ejercicio_4():
   matriz = [
       [1, 5, 3, 5],
       [8, 5, 9, 2],
       [4, 5, 6, 7]
   ]
   matriz1 = [
   ]
   suma=0
   for x in range(len(matriz)):
       for y in range(len(matriz[x])):
           suma+=matriz[x][y]
   suma/=12

   aux=[]
   for z in range(len(matriz)):
       for w in range(len(matriz[z])):
           if matriz[z][w] < suma:
                aux.append(suma)
           else:
               aux.append(matriz[z][w])
       matriz1.append(aux)
   print(matriz1)
   print(suma)
