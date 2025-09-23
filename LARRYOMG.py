
contactos_nombre = []
contactos_numero = []

ola = True
while ola:
    print("""
       Wasap

    1)Agregar contacto
    2)Mostrar un contacto
    3)Mostrar todos los contactos
    4)Salir

    """)

    op = int(input("ingrese una opcion:"))

    if op == 1:
        agregar_contacto_nombre = input("Ingrese el nombre de su contacto:")
        agregar_contacto_telefono = int(input("Ingrese el numero de su contacto:"))
        contactos_nombre.append(agregar_contacto_nombre)
        contactos_numero.append(agregar_contacto_telefono)

        print(f"¡Contactos añadidos con exito!")


    elif op == 2:
        buscar_contacto = str(input("Ingrese el nombre del contacto a buscar:"))
        if buscar_contacto in contactos_nombre:
       busco
            indice = contactos_nombre.index(buscar_contacto)
            print(f"""
            su contacto es:
            {contactos_nombre[indice], contactos_numero[indice]}
            """)

    elif op == 3:
        print(f"""Aqui estan todos sus contactos con sus respectivos numeros:
            Nombre:{contactos_nombre}
            telefono:{contactos_numero}
        """)

    else:
        pepe = False

