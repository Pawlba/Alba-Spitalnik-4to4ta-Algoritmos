def ejercicio1():
    lista = []
    n1 = int(input("Ingrese un número. "))
    lista.append(n1)
    n2 = int(input("Ingrese un número. "))
    lista.append(n2)
    n3 = int(input("Ingrese un número. "))
    lista.append(n3)
    n4 = int(input("Ingrese un número. "))
    lista.append(n4)
    n5 = int(input("Ingrese un número. "))
    lista.append(n5)
    for x in range(len(lista)):
        print(lista[x])


def ejercicio2():
    frutas = ["banana", "uva", "manzana"]
    fruta_buscar = input("¿Qué fruta desea buscar?")
    for x in range(len(frutas)):
        if fruta_buscar == frutas[x]:
            print(f"La fruta que desea buscar está en el índice {x}. ")
            break
    else:
        print("No se ha encontrado la fruta. ")


def ejercicio3():
    notas = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    notas_sumadas = sum(notas)
    promedio = notas_sumadas / 10
    print(promedio)


def ejercicio4():
    temperaturas = [-5, 30, 21, 24, 62, 39, 40, 41]
    maximo = 0
    minimo = 100000000000000000
    for x in temperaturas:
        if x > maximo:
            maximo = x
        if x < minimo:
            minimo = x
    print(f"La temperatura máxima fue de {maximo}°. ")
    print(f"La temperatura mínima fue de {minimo}°. ")

def ejercicio5():
    lista = [1, 6, 3, 8, 5, 89, 24, 62, 72]
    lista.sort()
    print(lista)

def ejercicio6():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    contador_par = 0
    contador_impar = 0
    for x in lista:
        if x % 2 == 0:
            contador_par += 1
        elif x % 2 == 1:
            contador_impar += 1
    print(f"La cantidad de números pares en la lista es de: {contador_par}")
    print(f"La cantidad de números impares en la lista es de: {contador_impar}")
ejercicio6()