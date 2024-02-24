from db_connection import insertar_registros, filtrar_usuarios_por_apellido, cambiar_genero_pelicula, eliminar_rentas_antiguas

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Insertar registros")
    print("2. Filtrar usuarios por apellido")
    print("3. Cambiar género de una película")
    print("4. Eliminar rentas antiguas")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ")
        if opcion == '1':
            insertar_registros()
        elif opcion == '2':
            # Ajusta el prompt para solicitar el apellido
            terminacion_apellido = input("Ingrese el final del apellido a buscar: ")
            filtrar_usuarios_por_apellido(terminacion_apellido)
        elif opcion == '3':
            nombre = input("Ingrese el nombre de la película: ")
            genero = input("Ingrese el nuevo género: ")
            cambiar_genero_pelicula(nombre, genero)
        elif opcion == '4':
            eliminar_rentas_antiguas()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()