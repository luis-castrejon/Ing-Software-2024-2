from faker import Faker  # Importa la librería Faker para generar datos aleatorios.
import pymysql.cursors  # Importa pymysql.cursors para interactuar con bases de datos MySQL.

# Función para conectar a la base de datos.
def get_db_connection():
    connection = pymysql.connect(host='localhost',  # Dirección del servidor de la base de datos.
                                user='luis',  # Nombre de usuario para la conexión.
                                password='Developer123!',  # Contraseña del usuario.
                                db='lab_ing_software',  # Nombre de la base de datos a la que se conecta.
                                port=3306,  # Puerto por el cual se realiza la conexión.
                                charset='utf8mb4',  # Codificación de caracteres utilizada.
                                cursorclass=pymysql.cursors.DictCursor)  # Tipo de cursor que retorna los resultados como diccionarios.
    return connection  # Retorna el objeto de conexión a la base de datos.

fake = Faker()  # Crea una instancia de Faker para generar datos aleatorios.

# Función para insertar un usuario en la base de datos.
def insertar_usuario(nombre, apPat, apMat, password, email):
    connection = get_db_connection()  # Obtiene una conexión a la base de datos.
    try:
        with connection.cursor() as cursor:  # Abre un cursor para ejecutar operaciones en la base de datos.
            # Define la sentencia SQL para insertar un nuevo usuario.
            sql_usuario = "INSERT INTO usuarios (nombre, apPat, apMat, password, email) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_usuario, (nombre, apPat, apMat, password, email))  # Ejecuta la sentencia SQL con los valores proporcionados.
            connection.commit()  # Confirma los cambios en la base de datos.
    finally:
        connection.close()  # Cierra la conexión a la base de datos.

# Función para insertar una película en la base de datos.
def insertar_pelicula(nombre, genero, duracion, inventario):
    connection = get_db_connection()  # Obtiene una conexión a la base de datos.
    try:
        with connection.cursor() as cursor:  # Abre un cursor para ejecutar operaciones en la base de datos.
            # Define la sentencia SQL para insertar una nueva película.
            sql_pelicula = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_pelicula, (nombre, genero, duracion, inventario))  # Ejecuta la sentencia SQL con los valores proporcionados.
            connection.commit()  # Confirma los cambios en la base de datos.
    finally:
        connection.close()  # Cierra la conexión a la base de datos.

# Función para borrar los datos generados en la base de datos.
def borrar_datos_generados():
    connection = get_db_connection()  # Obtiene una conexión a la base de datos.
    try:
        with connection.cursor() as cursor:  # Abre un cursor para ejecutar operaciones en la base de datos.
            # Borra todas las rentas, ya que tienen dependencias con usuarios y películas.
            cursor.execute("DELETE FROM rentar")
            connection.commit()  # Confirma los cambios en la base de datos.

            # Borra todas las películas y usuarios, que ya no tienen dependencias.
            cursor.execute("DELETE FROM peliculas")
            cursor.execute("DELETE FROM usuarios")
            connection.commit()  # Confirma los cambios en la base de datos.
    finally:
        connection.close()  # Cierra la conexión a la base de datos.

# Función para reiniciar los valores de autoincremento en las tablas de la base de datos.
def reiniciar_autoincremento():
    connection = get_db_connection()  # Obtiene una conexión a la base de datos.
    try:
        with connection.cursor() as cursor:  # Abre un cursor para ejecutar operaciones en la base de datos.
            # Reinicia el valor de autoincremento para la tabla de usuarios.
            cursor.execute("ALTER TABLE usuarios AUTO_INCREMENT = 13")
            # Reinicia el valor de autoincremento para la tabla de películas.
            cursor.execute("ALTER TABLE peliculas AUTO_INCREMENT = 1")
            # Reinicia el valor de autoincremento para la tabla de rentas.
            cursor.execute("ALTER TABLE rentar AUTO_INCREMENT = 2")
            connection.commit()  # Confirma los cambios en la base de datos.
    finally:
        connection.close()  # Cierra la conexión a la base de datos.

# Función para insertar datos aleatorios de usuarios y películas en la base de datos.
def insertar_datos_aleatorios(num_usuarios, num_peliculas):
    #reiniciar_autoincremento()  # (Opcional) Reinicia los valores de autoincremento antes de insertar datos.
    for _ in range(num_usuarios):  # Genera e inserta datos aleatorios para el número especificado de usuarios.
        nombre = fake.first_name()
        apPat = fake.last_name()
        apMat = fake.last_name()
        password = fake.password(length=12)
        email = fake.email()
        insertar_usuario(nombre, apPat, apMat, password, email)  # Inserta un usuario con los datos generados.

    for _ in range(num_peliculas):  # Genera e inserta datos aleatorios para el número especificado de películas.
        nombre = fake.word().title()
        genero = fake.word().title()
        duracion = fake.random_int(min=60, max=180)
        inventario = fake.random_int(min=1, max=20)
        insertar_pelicula(nombre, genero, duracion, inventario)  # Inserta una película con los datos generados.

# Ejemplo de cómo se llamaría la función para insertar datos aleatorios.
#insertar_datos_aleatorios(50, 15)  # Inserta 50 usuarios y 15 películas.

# Borrar datos generados y reiniciar autoincremento al final del script.
borrar_datos_generados()
reiniciar_autoincremento()