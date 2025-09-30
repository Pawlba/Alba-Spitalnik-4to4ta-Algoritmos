def calculadora_de_descuentos():
    precio_original= int(input("ingrese el precio original del producto"))
    if precio_original>=100:
        descuento=precio_original*0.15
    elif precio_original>=50:
        descuento=precio_original*0.10
    else:
        descuento=0
    precio_final=precio_original-descuento

def adivina_el_numero_secreto():
    numero_secreto=8
    while True:
        intento=int(input("Adivina el numero secreto"))
        if intento == numero_secreto:
            print("Felicidades, adivinaste el numero secreto:)")
        break
        if intento<numero_secreto:
            print("El numero ingresado es mayor al numero secreto")
        else:
            print("El numero ingresado es menor al numero secreto")
def contador_de_vocales():
    frase=input("ingrese una frase")
    vocales="aeiou"
    contador= 0
    for letra in frase:
        if letra in vocales:
def tabla_de_multiplicar():
        numero=int(input(("Ingrese un numero"))
         for i in range(1, 11)

def suma_de_numeros_pares():
    suma = 0
    while True:
        numero = int(input("Ingrese un número entero (0 para terminar): "))
        if numero == 0:
            break
        elif numero % 2 == 0:
            suma += numero
    print(f"La suma total de los números pares es: {suma}")




