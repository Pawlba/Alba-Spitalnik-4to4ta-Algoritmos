import mysql.connector  # librería para conectar con MySQL
from mysql.connector import errorcode  # códigos de error de mysql.connector
import datetime  # para manejar fechas
import json  # para volcar datos a JSON

cursor = None  # cursor de la base de datos (se inicializa en conectarBase)
cnx = None  # conexión a la base de datos (se inicializa en conectarBase)


# Conección a la base de datos
def conectarBase():
    global cnx, cursor
    # Se intenta conectar la base de datos
    try:
        cnx = mysql.connector.connect(user="root", password="", host="Localhost", database="farmacity")
        cursor = cnx.cursor(dictionary=True)  # cursor que devuelve filas como diccionarios
        print('Conexión establecida')
    # Si no se puede, se identifica el error
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuario o contraseña incorrectos!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('La base de datos no existe!')
        else:
            print(err)


conectarBase()  # conexión inicial al ejecutar la conexión



# Establecemos la consulta select dependiendo de la variable "Tabla"
def consultaSelect(tabla):
    Consulta = f"SELECT * FROM {tabla};"  # consulta dinámica(por depender de la tabla que se le ingrese)
    cursor.execute(Consulta)  # ejecuta la consulta con el cursor global
    return cursor.fetchall()  # retorna todas las filas como lista de diccionarios

def ordernarProductos():
    medicamentos = consultaSelect("medicamentos")  # carga actualizada desde BD
    lista = medicamentos  # alias local para manipular la lista
    n = len(lista)
    for i in range(n - 1):
        Hay_Cambio = False  # indicador para detectar si hubo intercambios en esta pasada
        for j in range(0, n - i - 1):  # no comparar los últimos i elementos ya ordenados
            if lista[j]["ID"] > lista[j + 1]["ID"]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # intercambio
                Hay_Cambio = True
        if not Hay_Cambio:
            break  # si no hubo cambios, la lista ya está ordenada
    return lista  # retorna la lista ordenada


def busquedaProducto(ID):
    arreglo = ordernarProductos()  # trabajar sobre lista ordenada por código
    valor = ID
    izquierda = 0
    derecha = len(arreglo) - 1
    # búsqueda binaria clásica
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arreglo[medio]["ID"] == valor:
            return arreglo[medio]  # retorna el diccionario del producto encontrado
        elif arreglo[medio]["ID"] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # no encontrado


def comprar():
    producto = busquedaProducto(int(input("Ingrese el ID del producto: ")))
    
    if producto == -1:
        print("Producto no encontrado.")
        return
    
    ID_producto = producto["ID"]
    stock = producto["stock"]  # obtener stock del producto encontrado
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    
    if cantidad > stock:
        print(f"Stock insuficiente. Solo hay {stock} unidades disponibles.")
        return
    
    fecha_compra = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Registrar la venta
    sql = "INSERT INTO ventas (ID_Medicamento, fecha, cantidad) VALUES (%s, %s, %s)"
    cursor.execute(sql, (ID_producto, fecha_compra, cantidad))
    
    # Actualizar el stock en la tabla medicamentos
    nuevo_stock = stock - cantidad
    sql_update = "UPDATE medicamentos SET stock = %s WHERE ID = %s"
    cursor.execute(sql_update, (nuevo_stock, ID_producto))
    
    cnx.commit()
    print(f"Compra registrada con éxito. Quedan {nuevo_stock} unidades en stock.")

comprar()