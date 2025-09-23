def ejercicio_1():
    matriz=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    aux=0
    for x in range(len(matriz)):
        for z in range(0, len(matriz[x]),3):
            aux+=matriz[x][z]
            print(aux)
def ejercicio_2():
    matriz=[[1,2,3],
            [4,5,6],
            [7,8,9]]
    suma_principal=0
    suma_secundaria=0
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            if x==y:
                suma_principal+=matriz[x][y]
            if x+y==2:
                suma_secundaria+=matriz[x][y]
    print(suma_secundaria,suma_principal)
def ejercicio_3():
    crear_matriz=int(input("ingrese un numero para crear una matriz cuadrada"))
    matriz=[]
    for x in range(0, crear_matriz):
        lita = []
        for y in range(0, crear_matriz):
            if x==y:
                lita.append(1)
            else:
                lita.append(0)
        matriz.append(lita)
    print(matriz)
ejercicio_3()