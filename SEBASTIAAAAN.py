import random
matriz = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
for c in range(0, 3):
    casillas=[]
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    for k in range(0, 3):
        matriz[x][y]=1
    print(matriz)
    casilla1= int(input("ingrese un numero de casilla"))
    casilla2=int(input("ingrese otro numero de casilla"))
    casillas.append(casilla1)
    casillas.append(casilla2)
    if matriz[x][y] in casillas:
            print("has descubierto un tesoro")
    else:
            print("oh no")
print(matriz)