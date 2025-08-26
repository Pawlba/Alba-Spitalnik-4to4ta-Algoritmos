import random
intentos=7
list1 = ["electroencefalografista", "anticonstitucionalidad", "esternocleidomastoideo", "otorrinolaringologico",
         "desoxirribonucleotido", "paralelepipedo"]
guiones = []
aleatorio = random.randint(0, 5)
palabra = list1[aleatorio]
largo = len(palabra)
for x in range(0, largo):#aca se utilizo un bucle for para hacer que el largo de la palabra a descubrir sea todo guiones#
    guiones.append("_")

   #--------------------------------------------------#

while intentos!=0:#en esta parte se utilizo un while para que mientras los intentos no sea 0 se siga corriendo y a su vez sacando intentos de a uno#
    print(f"intentos:{intentos}")
    print(guiones)
    variable=input("pon una letra:")
    intentos-=1

    #-------------------------------------------------#

    for y in range(0,largo):#para este bucle for se hizo que cada vez que pongas una letra que este en la palabra se quite un guion y agrege la letra adivinada en ese indice#
        if variable == palabra[y]:
            guiones[y] = variable

    #-------------------------------------------------#

    #en esta seccion se utilizaron los if para que en los casos que se adivine la palabra, no se adivine o la letra ingresada no este en la palabra, aparezca un mensaje#
    if variable not in palabra:
        print(f"intentos:{intentos}")
        print("la letra no esta en la palabra")
    if "_" not in guiones or variable==palabra:
        print("ganaste")
        break
    if "_" in guiones and intentos==0:
        print("perdiste")
#aca llore de felicidad por terminar el codigo#