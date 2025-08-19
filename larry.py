import random


def ejercicio1():
    CantidadActual = 1000
    mientras = True
    while mientras:
        try:
            print(f"""
                Banco Larry
                Saldo Actual:{CantidadActual}

                1)Retirar chips y multi
                2)Depositar chips y multi
                3)ser vencido por el balatro (salir)
            """)
            op = int(input("elija su opcion:"))
            if op == 1:
                CantidadRetirada = int(input("Elija la cantidad a retirar:"))
                if CantidadRetirada <= CantidadActual:
                    CantidadActual -= CantidadRetirada
            if op == 2:
                CantidadDepositada = int(input("ingrese la cantidad a depositar"))
                CantidadActual += CantidadDepositada
            if op == 3:
                print("fue humillado por Larry")
                mientras = False
        except ValueError:
            mientras = True
            print("Error, fue vencido por el Larry involuntariamente")


def ejercicio2():
    mientras = True
    while mientras:
        try:
            print("""
            Calculadora IMC

            1)Calcular
            2)Salir
            """)
            op = int(input("ingrese su opcion"))
            if op == 2:
                WHILE = False
                print("Cerrando programa")
            elif op == 1:
                Peso = float(input("ingrese su peso:"))
                Altura = float(input("ingrese su Altura:"))
                AlturaM = Altura * Altura
                IMC = Peso / AlturaM
                if IMC <= 18.0:
                    print(f"estas flaco{IMC}")
                elif IMC <= 24.9:
                    print(f"estas finisimo {IMC}")
                elif IMC >= 25:
                    print(f"estas gordo {IMC}")
        except ValueError:
            print("error elija la opcion de nuevo")


def ejercicio3():
    vocales = ["a", "e", "i", "o", "u"]
    seguimos = True
    while seguimos:
        try:
            frase = input("Ingrese una Frase: ")
            if frase == "agusfortnite2008":
                print("Nooo todo menos esoo")
                seguimos = False
            else:
                for vocales_a_buscar in range(0, len(vocales) - 1):
                    vocal_aleatoria = random.randint(0, 4)
                    frase = frase.replace(vocales[vocales_a_buscar], vocales[vocal_aleatoria])
                print(frase)
        except ValueError:
            print("Valor Inválido, Inténtelo de Nuevo: ")


def ejercicio4():
    seguimos = True
    frase_invertida = ""
    while seguimos:
        palabras_separadas = []
        frase = input("ingrese una frase: ")
        palabras_separadas = frase.split()
        print(palabras_separadas)
        for x in range(0, len(palabras_separadas)):
            palabras_separadas[x] = palabras_separadas[x][::-1]
        frase_invertida += " ".join(palabras_separadas)
        print(frase_invertida)


def ejercicio5():
    Lista_Nombres = []
    Seguimos = True

    while Seguimos:
        try:
            Ingreso_Usuario = int(input("""

                1. Ingresar alumno en lista
                2. Ver Alumno
                3. Salir
            """))
            if Ingreso_Usuario == 1:
                Nombre_a_Ingresar = input("Ingrese un nombre")
                Lista_Nombres.append(Nombre_a_Ingresar)
                Seguimos = True
            elif Ingreso_Usuario == 2:
                print("Lista de Alumnos", Lista_Nombres)
                Ver_Alumno = int(input("Ingrese indice de alumno"))
                print(Lista_Nombres[Ver_Alumno - 1])
                Seguimos = True
            elif Ingreso_Usuario == 3:
                print("chau")
                Seguimos = False
        except ValueError:
            print("Tipo de dato ingresado incorrecto")
        except IndexError:
            print("Indice de la lista no disponible")


ejercicio5()