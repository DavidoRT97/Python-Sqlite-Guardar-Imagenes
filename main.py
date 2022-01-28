"""
@title: GUARDAR Y RECUPERAR UNA IMAGEN EN SQLITE (ARCHIVO BLOB)
@author: David Reyes
@date: 2022/01/27
"""
import sqlite3

def guardarImagen():
    """[Con esta función guardamos una imagen en la BD SQLITE]

    Returns:
        [string]: [Mensaje de exito o fracaso]
    """
    try:
        # El 'rb' abre el archivo en formato binario para su lectura
        archivoImagen = open("python.jpg", "rb").read()
        # Nos conectamos a la BD
        con = sqlite3.connect("data.sqlite")
        cur = con.cursor()
        # La funcion Binary() es para especificar que el almacenamiento es binario
        buff = sqlite3.Binary(archivoImagen)
        # Ejecutamos el script
        cursor.execute("INSERT INTO bdImagen VALUES (?, ?);", ('PYTHON', buff,))
        # Guardamos los cambios y cerramos la conexion a la BD
        con.commit()
        con.close()
        return "¡DATOS GUARDADOS CON EXITO!"
    except Exception as e:return "¡ERROR!: {0]".format(e)

def recuperarImagen():
    """[Con esta función recuperamos una imagen en la BD SQLITE]

    Returns:
        [string]: [Mensaje de exito o fracaso]
    """
    try:
        # Nos conectamos a la BD y ejecutamos el script para recuperar información de la BD
        conexion = sqlite3.connect("data.sqlite")
        cursor = conexion.cursor()
        resultado = cursor.execute("SELECT archivoImagen FROM bdImagen;")
        # Creamos un nuevo archivo
        # 'wb' abre el archivo el archivo en formato binario para su escitura
        archivo = open("imagenRecuperada.jpg", "wb")
        archivo.write(resultado.fetchall()[0][0])
        # Cerramos el archivo, guardamos cambios en la BD y cerramos la conexion
        archivo.close()
        conexion.commit()
        conexion.close()
        return "¡IMAGEN RECUPERADA CON EXITO!"
    except Exception as e:return "¡ERROR!: {0]".format(e)

# Ejecutamos el codigo
dm = guardarImagen()
# Imprimimos en pantalla si la imagen se guardo con exito, de lo contrario nos mostrara el error que se provoco
print(dm)

#Recuperamos la imagen guardada
dm = recuperarImagen()
#Imprimimos en pantalla si recuperamos la imagen de la BD, de lo contrario nos mostrara el error que se provoco
print(dm)