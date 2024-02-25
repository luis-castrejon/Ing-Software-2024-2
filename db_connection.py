from faker import Faker  # Importa la librería Faker para generar datos aleatorios.
import pymysql.cursors  # Importa pymysql.cursors para interactuar con bases de datos MySQL.
import datetime # Importa datetime para manejar fechas y horas.
import random

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

def insertar_datos_aleatorios(num_usuarios, num_peliculas, num_rentas):
    peliculas_insertadas = 0
    intentos_fallidos = 0
    max_intentos_fallidos = 100  # Límite para evitar bucle infinito
    
    while peliculas_insertadas < num_peliculas and intentos_fallidos < max_intentos_fallidos:
        nombre = fake.word().title() + " " + fake.unique.word().title()  # Hacer nombre más único
        genero = fake.word().title()
        duracion = fake.random_int(min=60, max=180)
        inventario = fake.random_int(min=1, max=20)
        
        if insertar_pelicula(nombre, genero, duracion, inventario):
            peliculas_insertadas += 1
            print(f"Insertada: {nombre}")  # Para seguimiento
        else:
            intentos_fallidos += 1
            print(f"Fallido: {nombre}")  # Para seguimiento
    
    print(f"Películas insertadas: {peliculas_insertadas}. Intentos fallidos: {intentos_fallidos}.")
    fake.unique.clear()  # Reiniciar el generador único de Faker

# Función para insertar una película en la base de datos.
def insertar_pelicula(nombre, genero, duracion, inventario):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS cantidad FROM peliculas WHERE nombre = %s", (nombre,))
            resultado = cursor.fetchone()
            if resultado['cantidad'] > 0:
                return False  # No insertar si la película ya existe
            
            sql_pelicula = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql_pelicula, (nombre, genero, duracion, inventario))
            connection.commit()
            return True  # Confirmar inserción exitosa
    finally:
        connection.close()

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
            cursor.execute("ALTER TABLE usuarios AUTO_INCREMENT = 1")
            # Reinicia el valor de autoincremento para la tabla de películas.
            cursor.execute("ALTER TABLE peliculas AUTO_INCREMENT = 1")
            # Reinicia el valor de autoincremento para la tabla de rentas.
            cursor.execute("ALTER TABLE rentar AUTO_INCREMENT = 1")
            connection.commit()  # Confirma los cambios en la base de datos.
    finally:
        connection.close()  # Cierra la conexión a la base de datos.

# Función para insertar datos aleatorios de usuarios y películas en la base de datos.
def insertar_datos_aleatorios(num_usuarios, num_peliculas, num_rentas):
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
    
    # Obtiene listas de IDs existentes
    usuarios_ids = obtener_ids_usuarios()
    peliculas_ids = obtener_ids_peliculas()

    # Inserta rentas aleatorias
    for _ in range(num_rentas):
        idUsuario = random.choice(usuarios_ids)
        idPelicula = random.choice(peliculas_ids)
        fecha_renta = generar_fecha_renta_aleatoria()
        dias_de_renta = random.randint(1, 30)  # Ejemplo: Rentas de 1 a 30 días
        estatus = random.randint(0, 1)  # Ejemplo: 0 para no devuelto, 1 para devuelto

        insertar_renta(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus)

def obtener_ids_usuarios():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idUsuario FROM usuarios")
            return [row['idUsuario'] for row in cursor.fetchall()]
    finally:
        connection.close()

def obtener_ids_peliculas():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT idPelicula FROM peliculas")
            return [row['idPelicula'] for row in cursor.fetchall()]
    finally:
        connection.close()

def generar_fecha_renta_aleatoria():
    dias_atras = random.randint(1, 365)  # Genera una renta entre 1 y 365 días atrás
    fecha_renta = datetime.datetime.now() - datetime.timedelta(days=dias_atras)
    return fecha_renta.strftime('%Y-%m-%d %H:%M:%S')

def devolver_pelicula(idUsuario, idPelicula, fecha_devolucion):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            # Aquí se debería actualizar el estatus de la renta a devuelto (1)
            # Nota: Asegúrate de que la lógica de actualización coincida con tu esquema de base de datos y requisitos.
            sql_devolucion = "UPDATE rentar SET estatus = 1, fecha_devolucion = %s WHERE idUsuario = %s AND idPelicula = %s"
            cursor.execute(sql_devolucion, (fecha_devolucion, idUsuario, idPelicula))
            connection.commit()
    finally:
        connection.close()
        
#insertar_datos_aleatorios(50, 15, 100) # Inserta 50 usuarios, 15 películas y 100 rentas aleatorias.

# Borrar datos generados y reiniciar autoincremento al final del script.
#borrar_datos_generados()
#reiniciar_autoincremento()

def insertar_renta(idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=0):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql_renta = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql_renta, (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus))
            connection.commit()
    finally:
        connection.close()

def filtrar_usuarios_por_apellido(cadena):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql_filtro = "SELECT * FROM usuarios WHERE apPat LIKE %s OR apMat LIKE %s"
            cursor.execute(sql_filtro, ('%' + cadena, '%' + cadena))
            resultado = cursor.fetchall()
            for usuario in resultado:
                print(usuario)
    finally:
        connection.close()

def cambiar_genero_pelicula(nombre_pelicula, nuevo_genero):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql_actualizar = "UPDATE peliculas SET genero = %s WHERE nombre = %s"
            cursor.execute(sql_actualizar, (nuevo_genero, nombre_pelicula))
            connection.commit()
    finally:
        connection.close()

def eliminar_rentas_antiguas():
    fecha_limite = datetime.datetime.now() - datetime.timedelta(days=3)
    fecha_limite_str = fecha_limite.strftime('%Y-%m-%d %H:%M:%S')
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql_eliminar = "DELETE FROM rentar WHERE fecha_renta <= %s"
            cursor.execute(sql_eliminar, (fecha_limite_str,))
            connection.commit()
    finally:
        connection.close()
