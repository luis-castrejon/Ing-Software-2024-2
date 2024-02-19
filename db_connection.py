import pymysql.cursors

# Función para conectar a la base de datos
def get_db_connection():
    connection = pymysql.connect(host='localhost',
                                user='luis',
                                password='Developer123!',
                                db='lab_ing_software',
                                port=3306,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    return connection

def insertar_registros():
    # Establecer conexión
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql_usuario = "INSERT INTO usuarios (nombre, password, email) VALUES (%s, %s, %s)"
            cursor.execute(sql_usuario, ('Nombre Usuario', 'ContraseñaUsuario', 'usuario@example.com'))

            # Obtener el idUsuario del último registro insertado
            id_usuario = cursor.lastrowid

            sql_pelicula = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_pelicula, ('Nombre Pelicula', 'Genero', 120, 1))

            # Obtener el idPelicula del último registro insertado
            id_pelicula = cursor.lastrowid

            # Insertar en tabla 'rentar' asumiendo las llaves foráneas
            sql_rentar = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, NOW(), %s, %s)"
            cursor.execute(sql_rentar, (id_usuario, id_pelicula, 5, 0))

            connection.commit()
    finally:
        connection.close()

def filtrar_usuarios_por_nombre(terminacion_nombre):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM usuarios WHERE nombre LIKE %s"
            cursor.execute(sql, ('%' + terminacion_nombre))
            resultados = cursor.fetchall()
            for usuario in resultados:
                print(usuario)
    finally:
        connection.close()

def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
            cursor.execute(sql, (nuevo_genero, nombre_pelicula))
            connection.commit()
    finally:
        connection.close()

def eliminar_rentas_antiguas():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM rentar WHERE fecha_renta < DATE_SUB(CURDATE(), INTERVAL 3 DAY)"
            cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()
