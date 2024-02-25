from db_connection import insertar_datos_aleatorios, insertar_renta, filtrar_usuarios_por_apellido, cambiar_genero_pelicula, eliminar_rentas_antiguas, borrar_datos_generados, reiniciar_autoincremento, devolver_pelicula
from datetime import datetime

def menu_principal():
    while True:
        print("\nMenú Parte 1")
        print("1. Insertar datos aleatorios (usuarios, películas y rentas)")
        print("2. Rentar una película")
        print("3. Devolver una película")
        print("4. Filtrar usuarios por apellido")
        print("5. Cambiar el género de una película")
        print("6. Eliminar rentas antiguas")
        print("7. Limpiar la base de datos")
        print("8. Salir")

        try:
            opcion = input("Elige una opción: ")

            if opcion == '1':
                try:
                    num_usuarios = int(input("Número de usuarios a insertar: "))
                    num_peliculas = int(input("Número de películas a insertar: "))
                    num_rentas = int(input("Número de rentas a insertar: "))
                    insertar_datos_aleatorios(num_usuarios, num_peliculas, num_rentas)
                    print("Datos aleatorios insertados con éxito.")
                except ValueError:
                    print("Error: Por favor, introduce un número válido.")
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")

            elif opcion == '2':
                try:
                    idUsuario = int(input("ID del Usuario: "))
                    idPelicula = int(input("ID de la Película: "))
                    # Eliminamos la solicitud del estatus al usuario
                    while True:
                        fecha_str = input("Fecha de renta (YYYY-MM-DD HH:MM:SS): ")
                        try:
                            fecha_renta = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
                            break
                        except ValueError:
                            print("Formato de fecha incorrecto. Ejemplo correcto: 2024-01-23 15:30:00. Por favor, use el formato YYYY-MM-DD HH:MM:SS.")
                    dias_de_renta = int(input("Días de renta: "))
                    estatus = 0
                    insertar_renta(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus)
                    print("Renta insertada con éxito.")
                except ValueError:
                    print("Error: Por favor, introduce un número válido.")
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")

            elif opcion == '3':
                try:
                    idUsuario = int(input("ID del Usuario: "))
                    idPelicula = int(input("ID de la Película: "))
                    fecha_devolucion = input("Fecha de devolución (YYYY-MM-DD HH:MM:SS): ")
                    devolver_pelicula(idUsuario, idPelicula, fecha_devolucion)
                    print("Película devuelta con éxito.")
                except ValueError:
                    print("Error: Por favor, introduce un número válido.")
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")

            elif opcion == '4':
                try:
                    cadena = input("Cadena de búsqueda para el apellido: ")
                    filtrar_usuarios_por_apellido(cadena)
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")

            elif opcion == '5':
                try:
                    nombre_pelicula = input("Nombre de la película: ")
                    nuevo_genero = input("Nuevo género: ")
                    cambiar_genero_pelicula(nombre_pelicula, nuevo_genero)
                    print("Género actualizado con éxito.")
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")

            elif opcion == '6':
                try:
                    eliminar_rentas_antiguas()
                    print("Rentas antiguas eliminadas con éxito.")
                except Exception as e:
                    print(f"Ocurrió un error inesperado: {e}")

            elif opcion == '7':
                try:
                    borrar_datos_generados()
                    reiniciar_autoincremento()
                    print("La base de datos ha sido limpiada exitosamente.")
                except Exception as e:
                    print(f"Ocurrió un error al intentar limpiar la base de datos: {e}")

            elif opcion == '8':
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
                
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario. Saliendo...")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == '__main__':
    menu_principal()