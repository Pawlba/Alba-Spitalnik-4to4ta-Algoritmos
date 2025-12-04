def contando_hasta_diez():
    for numero in range(1, 11):
        print(numero)


def hola_5_veces():
    for i in range(1, 6):
        print("Hola Mundo BV")


def los_numeros_pares():
    for num in range(2, 21, 2):
        print(num)


def tabla_de_multiplicar_del_7():
    for n in range(7, 71, 7):
        print(n)


def suma_de_los_primeros_5_numeros():
    suma = 0
    for i in range(1, 6):
        suma += i
        print(suma)


def numero_positivo():
    num = int(input("Ingrese un numero: "))
    if num>0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")


def mayor_de_edad():
    edad = int(input("Ingrese la edad: "))
    if edad > 18:
        print("Bienvenido a la fiesta")
    else:
        print("Lo siento, eres muy joven")


def contrasenia_secreta():
    contrasenia = input("Ingrese la contrasenia: ")
    if contrasenia == "python123":
        print("La contrasenia es correcta, acceso concedido")
    else:
        print("¡Contraseña incorrecta, Autodestrucción en 5 minutos!")


def par_o_impar():
    num = int(input("Ingrese un numero: "))
    if num%2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")


def entrada_gratis():
    edad = int(input("Ingrese su edad: "))
    palomitas = input("Ha comprado palomirtas antes?:  (Si/No)" )
    if edad > 65 and palomitas == "Si":
        print("Felicidades, tienes entrada gratuita al cine")
    else:
        print("Compra la entrada o raja de aca")

def despegue():
    i = 5
    while i > 0:
        print(i)
        print("Listo para despegar")
        i -= 1
    print("Despegue")


def numero_secreto():
    num_secreto = 7
    while True:
        num = int(input("Adivina el numero: "))
        if num == num_secreto:
            print("Felicidades, adivinaste el numero")
            break


def muchas_sumas():
    suma = 0
    while True:
        num = input("Ingrese varios numeros a sumar (0 para finalizar :b): ")
        if num == "0":
            break
        suma += int(num)
    print(f"La suma total es: {suma}")


