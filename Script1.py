def solicitar_nombres_jugadores():
    """
    Solicita al usuario ingresar los nombres de dos jugadores y los devuelve en una lista.
    
    Returns:
    nombres (list): Lista con los nombres de los jugadores ingresados.
    """
    nombres = []
    for i in range(1, 3):
        while True:
            try:
                nombre = input(f"Ingrese el nombre del Jugador {i}: ")
                if nombre.isalpha():
                    nombres.append(nombre)
                    break
                else:
                    print("Entrada inválida. Por favor, ingrese solo letras.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese solo letras.")
    return nombres

def solicitar_punto(jugadores):
    """
    Solicita al usuario el número de jugador que ganó el punto.

    Parameters:
    jugadores (list): Lista de jugadores.

    Returns:
    int: El índice del jugador que ganó el punto.
    """
    while True:
        try:
            ganador_punto = input(f"\nIngrese el número de jugador que ganó el punto (1 o 2): ")
            if ganador_punto in ["1", "2"]:
                return int(ganador_punto) - 1
            else:
                print("Entrada inválida. Por favor, ingrese '1' o '2'.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

def actualizar_puntos(puntos, jugador):
    """
    Actualiza los puntos de un jugador en un juego de tenis.

    Parámetros:
    puntos (list): Una lista que contiene los puntos de ambos jugadores.
    jugador (int): El índice del jugador cuyos puntos se van a actualizar.

    Retorna:
    list: Una lista actualizada con los puntos de ambos jugadores.

    """
    # Definimos la secuencia de puntuación hasta 40
    secuencia_puntos = ["0", "15", "30", "40"]
    
    if puntos[jugador] == "40" and puntos[1-jugador] == "40":
        puntos[jugador] = "Adv."
    elif puntos[jugador] == "Adv.":
        puntos[jugador] = "Gana"
    elif puntos[1-jugador] == "Adv.":
        puntos[1-jugador] = "40"
    else:
        # Actualizar el puntaje normalmente hasta llegar a 40
        indice_actual = secuencia_puntos.index(puntos[jugador])
        if indice_actual < 3:  # Actualiza el punto hasta "40"
            puntos[jugador] = secuencia_puntos[indice_actual + 1]
        elif indice_actual == 3 and puntos[1-jugador] != "40":
            # Si el oponente no tiene 40, entonces al llegar a 40 el jugador gana el punto
            puntos[jugador] = "Gana"
    
    return puntos

def verificar_ganador_juego(puntos, jugador):
    """
    Verifica si el jugador ha ganado el juego.

    Args:
        puntos (dict): Un diccionario que contiene los puntos de cada jugador.
        jugador (str): El nombre del jugador a verificar.

    Returns:
        bool: True si el jugador ha ganado, False en caso contrario.
    """
    return puntos[jugador] == "Gana"

def verificar_ganador_set(juegos, sets, jugador):
    """
    Verifica si un jugador ha ganado el set.

    Args:
        juegos (list): Lista de juegos ganados por cada jugador.
        sets (list): Lista de sets ganados por cada jugador.
        jugador (int): Índice del jugador actual.

    Returns:
        bool: True si el jugador ha ganado el set, False en caso contrario.
    """
    if juegos[jugador] >= 6 and (juegos[jugador] - juegos[1-jugador] >= 2):
        sets[jugador] += 1
        return True
    return False

def imprimir_marcador(jugadores, puntos, juegos, sets):
    """
    Imprime el marcador del juego actual, los juegos y los sets de un partido de tenis.

    Args:
        jugadores (list): Lista con los nombres de los jugadores.
        puntos (list): Lista con los puntos de cada jugador en el juego actual.
        juegos (list): Lista con los juegos ganados por cada jugador en el set actual.
        sets (list): Lista con los sets ganados por cada jugador en el partido.

    Returns:
        None
    """
    print()
    formato_linea = "{:>22} {:<}" 
    print(formato_linea.format("Sets:", "{} {} - {} {}".format(jugadores[0], sets[0], sets[1], jugadores[1])))
    print(formato_linea.format("Juegos (Set Actual):", "{} {} - {} {}".format(jugadores[0], juegos[0], juegos[1], jugadores[1])))
    print(formato_linea.format("Puntos (Juego Actual):", "{} {} - {} {}".format(jugadores[0], puntos[0], puntos[1], jugadores[1])))

def verificar_cambio_cancha(juegos):
    """
    Verifica si es necesario realizar un cambio de cancha en base a la suma de los juegos.

    Args:
        juegos (list): Una lista de enteros representando la cantidad de juegos jugados en cada cancha.

    Returns:
        bool: True si la suma de los juegos es impar, False en caso contrario.
    """
    total_juegos = sum(juegos)
    if total_juegos % 2 == 1:  # Si la suma de los juegos es impar, se realiza cambio de cancha
        return True
    return False

def imprimir_cambio_cancha(juegos, juego_actual_finalizado):
    """
    Imprime un mensaje de cambio de cancha si el juego actual ha finalizado y el total de juegos es impar.

    Args:
        juegos (list): Lista de juegos.
        juego_actual_finalizado (bool): Indica si el juego actual ha finalizado.

    Returns:
        None
    """
    total_juegos = sum(juegos)
    if juego_actual_finalizado and total_juegos % 2 == 1:
        print("\nCambio de cancha.\n")

def main():
    """
    Función principal que ejecuta el juego de tenis.

    La función solicita los nombres de los jugadores, inicializa las variables necesarias
    para llevar el marcador del juego, los juegos y los sets. Luego, se ejecuta un bucle
    hasta que uno de los jugadores haya ganado dos sets.

    En cada iteración del bucle, se muestra el sacador actual, se solicita el ganador del punto,
    se actualizan los puntos, se verifica si hay un ganador del juego y se actualizan los juegos
    y el sacador para el siguiente juego. Además, se imprime el marcador y se verifica si hay
    cambio de cancha después de finalizar un juego.

    Al finalizar el bucle, se determina y anuncia el ganador del partido.

    """
    jugadores = solicitar_nombres_jugadores()
    puntos = ["0", "0"]
    juegos = [0, 0]
    sets = [0, 0]
    sacador = 0  # Asume que el jugador 1 comienza sacando

    while sets.count(2) == 0:
        print(f"\nSacador actual: {jugadores[sacador]}")  # Indica quién es el sacador al inicio de cada juego
        ganador_punto = solicitar_punto(jugadores)
        puntos = actualizar_puntos(puntos, ganador_punto)
        juego_actual_finalizado = False
        if verificar_ganador_juego(puntos, ganador_punto):
            juegos[ganador_punto] += 1
            puntos = ["0", "0"]  # Reinicia los puntos para el nuevo juego
            sacador = 1 - sacador  # Cambia el sacador para el siguiente juego
            print(f"\nEl próximo sacador será: {jugadores[sacador]}")  # Anuncia quién será el próximo sacador
            juego_actual_finalizado = True

            if verificar_ganador_set(juegos, sets, ganador_punto):
                juegos = [0, 0]  # Reinicia los juegos para el nuevo set
        
        imprimir_marcador(jugadores, puntos, juegos, sets)  # Asegura que esta llamada se hace después de todas las actualizaciones
        imprimir_cambio_cancha(juegos, juego_actual_finalizado)  # Verifica e imprime si hay cambio de cancha después de finalizar un juego

    # Determina y anuncia el ganador del partido
    ganador_set = 0 if sets[0] == 2 else 1
    print(f"\n{jugadores[ganador_set]} gana el partido!")

if __name__ == "__main__":
    main()