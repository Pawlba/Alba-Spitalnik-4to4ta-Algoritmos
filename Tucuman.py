def diccionario_de_informacion_personal():
    informacion_personal={
        "nombre": "Alba",
        "edad":16,
        "ciudad": "Tucuman",
        "profesion": "Abastesedora logistica en lugares de poca concentracion"
    }
    print(informacion_personal)
def modificacion_valores():
    informacion_personal = {
        "nombre": "Alba",
        "edad": 16,
        "ciudad": "Tucuman",
        "profesion": "Abastesedora logistica en lugares de alta concentracion",
        "email": "chuchamandarina@gmail.com",
        "telefono": 1133446618
    }
    informacion_personal["profesion"] = "Abastesedora logistica"
    informacion_personal["ciudad"] = "La rioja"
    print(informacion_personal)
def diccionario_de_calificaciones():
    calificaciones_alumnos = {
        "matematica": 9,
        "lengua": 7,
        "quimica": 8,
        "fisica": 5
    }
def promedio_de_calificaciones():
    calificaciones_alumnos = {
        "matematica": 9,
        "lengua": 7,
        "quimica": 8,
        "fisica": 5
    }
    math=calificaciones_alumnos["matematica"]
    lengua=calificaciones_alumnos["lengua"]
    quimica=calificaciones_alumnos["quimica"]
    fisica=calificaciones_alumnos["fisica"]
    sum= math+lengua+quimica+fisica
    promedio=sum/4
    print(promedio)
def diccionario_de_paises_y_capitales():
    paises_y_capitales = {
        "Argentina": "Buenos Aires",
        "Canada": "Ottawa",
        "España": "Madrid",
        "Brasil": "Brasilia"
    }
    usuario=input("Ingrese un pais")
    print(f"Su capital es: {paises_y_capitales[usuario]}")
def diccionario_de_precios():
    precios_productos = {
        "Fideos": 45,
        "Arroz": 80,
        "Polenta": 7
    }
    productos=input("Ingrese su producto")
    cantidad=int(input("Ingrese la cantidad de productos"))
    total=precios_productos[productos]*cantidad
    print(total)
def eliminando_elementos():
    informacion_personal = {
        "nombre": "Alba",
        "edad": 16,
        "ciudad": "Tucuman",
        "profesion": "Abastesedora logistica en lugares de alta concentracion",
        "email": "chuchamandarina@gmail.com",
        "telefono": 1133446618
    }
    del informacion_personal["telefono"]
    print(informacion_personal)
def verificando_la_existencia_de_una_clave():
        informacion_personal = {
            "nombre": "Alba",
            "edad": 16,
            "ciudad": "La rioja",
            "Trabajo": "Abastecedor logistica",
            "telefono": 1133446618,
            "email": "chuchamandarina@gmail.com"
        }
        clave = input("ingrese una clave")
        if clave in informacion_personal:
            print("True")
        else:
            print("False")

verificando_la_existencia_de_una_clave()
def combinando_diccionarios():
    jugadores={
        "Jugador1": "Lionel Messi",
        "jugador2": "Kylian Mbappe",
        "jugador3": "Erling Haañamd",
        "jugador4": "Vinicius Junior"
    }
    equipos={
        "equipo1":"Inter Miami CF",
        "equipo2": "Real Madrid",
        "equipo3": "Manchester city",
        "equipo4": "Real Madrid"
    }
    jugadores_y_equipos=jugadores|equipos
    print(jugadores_y_equipos)



