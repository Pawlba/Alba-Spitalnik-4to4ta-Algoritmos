def prueba_matrices():
    palos= ['Picas', 'Tréboles', 'Diamantes', 'Corazones']
    valores= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    valores_cartas = []
    for valor in valores:
        if valor == 1:
            valores_cartas.append('A')
        elif valor == 11:
            valores_cartas.append('J')
        elif valor == 12:
            valores_cartas.append('Q')
        elif valor == 13:
            valores_cartas.append('K')
        else:
            valores_cartas.append(str(valor))

    mazo = [[0 for i in range(2)] for o in range(52)]
    indice = 0
    for palo in palos:
        for valor in valores_cartas:
            mazo[indice][0] = palo
            mazo[indice][1] = valor
            indice += 1

    valor_total = 0
    for carta in mazo:
        if carta[1] in ['J', 'Q', 'K']:
            valor_total += 10
        elif carta[1] == 'A':
            valor_total += 1
        else:
            valor_total += int(carta[1])

    print("Matriz del mazo:")
    for carta in mazo:
        print(carta)
    print("El valo total de chips es:", [valor_total])

prueba_matrices()