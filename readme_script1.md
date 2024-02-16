## Descripción

Este script simula el marcador de un partido de tenis, implementando las reglas básicas del juego, incluyendo el manejo de puntos, juegos, sets, ventajas, y el cambio de cancha. Está diseñado para ser interactivo, permitiendo a los usuarios ingresar el ganador de cada punto y observar el estado actual del marcador.

### Cómo Ejecutar
Para ejecutar este script, antes activa el entorno virtual. Después inicia el script desde la línea de comandos de la siguiente manera:

`python3 Script1.py`

- Al inicio, se te pedirá que ingreses los nombres de los dos jugadores participantes.
- Durante el juego, se solicitará ingresar el número del jugador que ganó el punto (1 o 2). Debes ingresar '1' si el primer jugador gana el punto, o '2' si es el segundo jugador.

## Funcionamiento

El script comienza solicitando los nombres de los dos jugadores para personalizar la experiencia. Después de cada punto, el usuario debe indicar qué jugador ganó el punto.

El script actualiza los puntos, juegos, y sets basándose en las reglas del tenis, incluyendo el manejo de situaciones de 40-40 y ventaja.

Se indica un cambio de cancha después de cada juego impar, basándose en la suma total de juegos.

El partido termina cuando uno de los jugadores gana la mayoría de los sets planeados (mejor de 3 para este script).

### Decisiones de Diseño
- Después de un 40-40, un jugador necesita ganar dos puntos consecutivos para ganar el juego.
- El script alterna automáticamente el jugador que saca después de cada juego.
- El script no implementa tiebreaks en sets 6-6. El juego continúa hasta que uno de los jugadores logre una ventaja de dos juegos.

El script incluye dos `try-except` para manejar entradas inválidas, asegurando que el usuario solo pueda ingresar valores apropiados durante el juego.