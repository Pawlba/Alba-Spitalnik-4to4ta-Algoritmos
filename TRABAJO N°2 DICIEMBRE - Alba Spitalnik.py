import random
def parte2_ejercicio_uno():
    frutas = ["manzana", "banana", "cereza"]
    print(frutas)
    print(frutas[1])

def ejercicio_dos():
    animales = ["perro", "gato", "elefante"]
    animales.remove("gato")
    animales.append("jirafa")
    print(animales)

def ejercicio_tres():
    lista1 = [5, 1, 8]
    lista2 = [3, 9, 2]
    lista_combinada = lista1 + lista2
    valor_total = 0
    for num in lista_combinada:
        valor_total = valor_total + num
    print(valor_total)


def ejercicio_cuatro():
    lista1 = [5, 1, 8]
    lista2 = [3, 9, 2]
    lista_combinada = lista1 + lista2
    print(lista_combinada)


def ejercicio_cinco():
    nombres = ["Pepe", "Juana", "Santiago", "Ignacio", "Federico", "Gabriel", "Sofia"]
    notas = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
    alumno = []
    alumno.append(nombres[0])
    alumno.append(notas[0])
    print(alumno)

def ejercicio_seis():
    nota1 = (random.randint(1, 10))
    nota2 = (random.randint(1, 10))
    nota3 = (random.randint(1, 10))
    alumno1 = ["Pepe", nota1]
    alumno2 = ["Juana", nota2]
    alumno3 = ["Santiago", nota3]
    notas_curso = [alumno1[1], alumno2[1], alumno3[1]]
    promedio = (notas_curso[0] + notas_curso[1] + notas_curso[2])/3
    return promedio

def ejercicio_siete():
    seguimos = True
    while seguimos:
        promedio_escuela1 = ejercicio_seis()
        promedio_escuela2 = ejercicio_seis()
        promedio_escuela3 = ejercicio_seis()
        opcion = input("Presione 1 para generar un curso o 2 para salir")
        if opcion == "2":
            print("Cerrando programa")
            seguimos = False
        elif opcion == "1":
            promedio = promedio_escuela1 + promedio_escuela2 + promedio_escuela3
            promedio = promedio / 3
            print(promedio)
            if promedio>=6:
                print("Las escuelas tienen buen promedio")
            else:
                print("Las escuelas tienen malos promedios")

