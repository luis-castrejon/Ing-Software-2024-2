from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from modelos.usuario import Base as BaseUsuario, Usuario
from modelos.pelicula import Base as BasePelicula, Pelicula
from modelos.renta import Base as BaseRenta, Renta
from datetime import datetime
from crud.operaciones import (
    obtener_usuarios, obtener_usuario_por_id,
    actualizar_usuario, eliminar_usuario,
    obtener_peliculas, obtener_pelicula_por_id,
    actualizar_pelicula, eliminar_pelicula,
    obtener_rentas, obtener_renta_por_id,
    actualizar_renta, eliminar_renta, eliminar_todos_los_registros
)

# Configuración de la conexión
engine = create_engine('mysql+pymysql://luis:Developer123!@localhost/lab_ing_software')
Session = sessionmaker(bind=engine)
session = Session()

# Creación de todas las tablas basadas en los modelos
BaseUsuario.metadata.create_all(engine)
BasePelicula.metadata.create_all(engine)
BaseRenta.metadata.create_all(engine)

def confirmar_accion(mensaje="¿Estás seguro? (s/n): "):
    respuesta = input(mensaje).lower()
    return respuesta == 's'

def menu_principal():
    while True:
        print("\nMenú Principal:")
        print("1. Ver registros de una tabla")
        print("2. Filtrar registros de una tabla por ID")
        print("3. Actualizar un registro")
        print("4. Eliminar un registro")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        try:
            if opcion == "1":
                # Ver registros
                tipo = int(input("Elige el tipo de registro (1: Usuario, 2: Pelicula, 3: Renta): "))
                if tipo == 1:
                    usuarios = obtener_usuarios(session)
                    for usuario in usuarios:
                        print(usuario)
                elif tipo == 2:
                    peliculas = obtener_peliculas(session)
                    for pelicula in peliculas:
                        print(pelicula)
                elif tipo == 3:
                    rentas = obtener_rentas(session)
                    for renta in rentas:
                        print(renta)
            elif opcion == "2":
                # Filtrar registros por ID
                tipo = int(input("Elige el tipo de registro para filtrar por ID (1: Usuario, 2: Pelicula, 3: Renta): "))
                id = int(input("Ingresa el ID: "))
                if tipo == 1:
                    usuario = obtener_usuario_por_id(session, id)
                    print(usuario if usuario else "Usuario no encontrado.")
                elif tipo == 2:
                    pelicula = obtener_pelicula_por_id(session, id)
                    print(pelicula if pelicula else "Película no encontrada.")
                elif tipo == 3:
                    renta = obtener_renta_por_id(session, id)
                    print(renta if renta else "Renta no encontrada.")
            elif opcion == "3":
                tipo = int(input("Elige el tipo de registro (1: Usuario, 2: Pelicula, 3: Renta): "))
                id = int(input("Ingresa el ID del registro a actualizar: "))

                if tipo == 1:  # Actualizar Usuario
                    nuevo_nombre = input("Nuevo nombre del usuario: ")
                    actualizar_usuario(session, id, nombre=nuevo_nombre)
                    print("Usuario actualizado.")
                elif tipo == 2:  # Actualizar Pelicula
                    nuevo_nombre = input("Nuevo nombre de la película: ")
                    actualizar_pelicula(session, id, nombre=nuevo_nombre)
                    print("Película actualizada.")
                elif tipo == 3:  # Actualizar Renta
                    nueva_fecha_renta = input("Nueva fecha de renta (YYYY-MM-DD HH:MM:SS): ")
                    try:
                        fecha_renta = datetime.strptime(nueva_fecha_renta, "%Y-%m-%d %H:%M:%S")
                        actualizar_renta(session, id, fecha_renta=fecha_renta)
                        print("Fecha de renta actualizada correctamente.")
                    except ValueError:
                        print("Formato de fecha y hora no válido. Asegúrate de usar el formato YYYY-MM-DD HH:MM:SS.")
            elif opcion == "4":
                # Eliminar un registro o todos los registros
                decision = input("¿Deseas borrar 'todos' los registros de la base de datos o solo 'uno' en específico? Escribe 'todos' o 'uno': ")
                if decision.lower() == 'todos':
                    if confirmar_accion("¿Confirmas la eliminación de todos los registros de la base de datos? (s/n): "):
                        eliminar_todos_los_registros(session)
                        print("Todos los registros de la base de datos han sido eliminados.")
                if decision.lower() == 'uno':
                    while True:
                        tipo = int(input("Elige el tipo de registro para eliminar (1: Usuario, 2: Pelicula, 3: Renta): "))
                        id = input("Ingresa el ID del registro a eliminar: ")

                        if tipo == 1:
                            usuario = obtener_usuario_por_id(session, id)
                            if usuario:
                                eliminar_usuario(session, id)
                                print(f"Usuario con ID {id} eliminado.")
                                break
                            else:
                                print(f"No se encontró un usuario con ID {id}. Por favor, intenta nuevamente.")
                        elif tipo == 2:
                            pelicula = obtener_pelicula_por_id(session, id)
                            if pelicula:
                                eliminar_pelicula(session, id)
                                print(f"Película con ID {id} eliminada.")
                                break
                            else:
                                print(f"No se encontró una película con ID {id}. Por favor, intenta nuevamente.")
                        elif tipo == 3:
                            renta = obtener_renta_por_id(session, id)
                            if renta:
                                eliminar_renta(session, id)
                                print(f"Renta con ID {id} eliminada.")
                                break
                            else:
                                print(f"No se encontró una renta con ID {id}. Por favor, intenta nuevamente.")
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
        except Exception as e:
            print(f"Error: {e}. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()