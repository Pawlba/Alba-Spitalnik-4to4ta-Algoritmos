def ejercicio1():
    list1=["Dada", "una", "lista", "de", "palabras", "escribir", "un", "programa", "que", "use", "un", "bucle", "for", "para", "encontrar", "y", "mostrar", "la", "palabra", "con", "la", "mayor", "cantidad", "de", "caracteres"]
    lamasgrande=""
    for x in range(0, len(list1)):
        if len(lamasgrande) < len(list1[x]):
            lamasgrande=list1[x]
    print(lamasgrande)
def ejercicio2():
    list1=["Dada", "una", "lista", "de", "palabras", "escribir", "un", "programa", "que", "use", "un", "bucle", "for", "para", "encontrar", "y", "mostrar", "la", "palabra", "con", "la", "mayor", "cantidad", "de", "caracteres"]
    vocales="AEIOUaeiou"
    auxiliar=0
    for x in list1:
        for y in x:
            if y in vocales:
                auxiliar += 1
    print(auxiliar)
def ejercicio3():
    list1=[1,2,3,4,5,6,7,8,9,10]
    list2=[]
    numero=int(input("ingrese un numero:"))
    for x in range(0, len(list1)):
        list2.append(numero*list1[x])
    print(list2)
import random

def dar_carta():
    posiblesNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    posiblesPalos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    carta = []
    aleatorio = random.randint(0,12)
    carta.append(posiblesNumeros[aleatorio])
    aleatorio = random.randint(0, 3)
    carta.append(posiblesPalos[aleatorio])
    return carta

def ejercicio4():
    mano_guardada=[]
    pepe=True
    while pepe:
        opcion=int(input(f"""
                Balatro
        mano{mano_guardada}
        1)Dar cartas
        2)Descartar
        3)Dejar de jugar
        
        """))
        if opcion==1:
            for x in range(8):
                mano_guardada.append(dar_carta())
            print(f"tu mano es:{mano_guardada}")
            pepe = True
        elif opcion==2:
             descarte = int(input("cuantas cartas queres descartar"))
             for x in range(0, descarte):
                print(mano_guardada)
                cartas_descartar=int(input("elija la carta a descartar por su indice(max5):"))
                mano_guardada.pop(cartas_descartar)
             for y in range(0,descarte):
                 mano_guardada.append(dar_carta())
        elif opcion==3:
            pepe = False
ejercicio4()

