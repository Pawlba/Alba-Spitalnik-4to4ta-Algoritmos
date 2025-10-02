import random
def borrachino_chino():
    camino = ["0", "1", "2", "3", "4", "5", "6", "7 ", "8", "9"]
    posicion = 5
    camino = [posicion]
    pasos = 0

    while posicion != 0 and posicion != 9:
        numero_aleatorio = random.randint(0, 1)
        if numero_aleatorio == 0:
            if posicion > 0:
                posicion -= 1
            else:
                if posicion < len(camino) - 1:
                    posicion += 1
                camino.append(posicion)
                pasos += 1
    print(f"Camino recorrido {camino}")
    print(f"pasos necesarios {pasos}")

borrachino_chino()
