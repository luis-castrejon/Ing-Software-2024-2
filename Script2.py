def contar_valles(recorrido):
    """
    Función para contar el número de valles en un recorrido dado.
    Un valle se define como una secuencia que comienza con un paso hacia abajo 'D' desde el nivel del mar y termina cuando se regresa al nivel del mar.

    :param recorrido: Cadena de caracteres que representa el recorrido del caminante, donde 'Ú' es un paso hacia arriba y 'D' es un paso hacia abajo.
    :return: El número de valles atravesados.
    """

    # Inicialización de variables
    nivel_del_mar = 0  # Representa la altura actual durante el recorrido, inicia en 0 (nivel del mar).
    contador_de_valles = 0  # Contador para el número de valles atravesados.
    en_valle = False  # Flag para controlar si el caminante está actualmente en un valle.

    # Iterar a través de cada paso en el recorrido
    for paso in recorrido:
        # Verificar si el paso actual es hacia arriba 'Ú'
        if paso == 'U':
            nivel_del_mar += 1  # Incrementar el nivel del mar si el paso es hacia arriba.
            # Verificar si con este paso se sale de un valle, es decir, se vuelve al nivel del mar
            if nivel_del_mar == 0 and en_valle:
                contador_de_valles += 1  # Incrementar el contador de valles.
                en_valle = False  # Actualizar el flag indicando que ya no se está en un valle.
        else:  # El paso es hacia abajo 'D'
            # Si se va a entrar a un valle (primer paso hacia abajo desde el nivel del mar)
            if nivel_del_mar == 0:
                en_valle = True  # Actualizar el flag indicando que se está entrando a un valle.
            nivel_del_mar -= 1  # Decrementar el nivel del mar si el paso es hacia abajo.

    # Retornar el número total de valles atravesados durante el recorrido
    return contador_de_valles

# Ejemplo
recorrido = "DDUDDUUUDUDDDDUUUDUDUU"
print("Recorrido: ", recorrido)
print("Número de valles atravesados:", contar_valles(recorrido))
print()






class Nodo:
    """
    Clase que representa un nodo en un árbol de búsqueda binaria.

    Atributos:
        izquierda: El nodo hijo izquierdo.
        derecha: El nodo hijo derecho.
        valor: El valor almacenado en el nodo.

    Métodos:
        __init__(clave): Constructor de la clase Nodo.
    """
    def __init__(self, clave):
        """
        Constructor de la clase Nodo.
        
        Parámetros:
        - clave: el valor que se asignará al nodo.
        """
        self.izquierda = None
        self.derecha = None
        self.valor = clave

class ArbolDeBusquedaBinaria:
    """
    Clase que representa un árbol de búsqueda binaria.

    Atributos:
        raiz: El nodo raíz del árbol.

    Métodos:
        insertar(clave): Inserta un nuevo nodo con la clave especificada en el árbol.
        preorden(): Devuelve una lista con los valores del árbol en recorrido preorden.
        inorden(): Devuelve una lista con los valores del árbol en recorrido inorden.
        postorden(): Devuelve una lista con los valores del árbol en recorrido postorden.
    """

    def __init__(self):
        """
        Constructor de la clase.
        Inicializa el atributo 'raiz' como None.
        """
        self.raiz = None

    def insertar(self, clave):
        """
        Inserta un nuevo nodo con la clave especificada en el árbol.

        Args:
            clave: La clave del nuevo nodo a insertar.
        """
        if self.raiz is None:
            self.raiz = Nodo(clave)
        else:
            self._insertar_recursivo(self.raiz, clave)

    def _insertar_recursivo(self, nodo_actual, clave):
        """
        Método auxiliar para insertar un nuevo nodo de forma recursiva.

        Args:
            nodo_actual: El nodo actual en el proceso de inserción.
            clave: La clave del nuevo nodo a insertar.
        """
        if clave < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(clave)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, clave)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(clave)
            else:
                self._insertar_recursivo(nodo_actual.derecha, clave)

    def preorden(self):
        """
        Devuelve una lista con los valores del árbol en recorrido preorden.

        Returns:
            Una lista con los valores del árbol en recorrido preorden.
        """
        return self._preorden_recursivo(self.raiz, [])

    def _preorden_recursivo(self, nodo_actual, resultado):
        """
        Método auxiliar para realizar el recorrido preorden de forma recursiva.

        Args:
            nodo_actual: El nodo actual en el proceso de recorrido.
            resultado: La lista que almacenará los valores del recorrido.

        Returns:
            La lista con los valores del recorrido preorden.
        """
        if nodo_actual:
            resultado.append(nodo_actual.valor)
            self._preorden_recursivo(nodo_actual.izquierda, resultado)
            self._preorden_recursivo(nodo_actual.derecha, resultado)
        return resultado

    def inorden(self):
        """
        Devuelve una lista con los valores del árbol en recorrido inorden.

        Returns:
            Una lista con los valores del árbol en recorrido inorden.
        """
        return self._inorden_recursivo(self.raiz, [])

    def _inorden_recursivo(self, nodo_actual, resultado):
        """
        Método auxiliar para realizar el recorrido inorden de forma recursiva.

        Args:
            nodo_actual: El nodo actual en el proceso de recorrido.
            resultado: La lista que almacenará los valores del recorrido.

        Returns:
            La lista con los valores del recorrido inorden.
        """
        if nodo_actual:
            self._inorden_recursivo(nodo_actual.izquierda, resultado)
            resultado.append(nodo_actual.valor)
            self._inorden_recursivo(nodo_actual.derecha, resultado)
        return resultado

    def postorden(self):
        """
        Devuelve una lista con los valores del árbol en recorrido postorden.

        Returns:
            Una lista con los valores del árbol en recorrido postorden.
        """
        return self._postorden_recursivo(self.raiz, [])

    def _postorden_recursivo(self, nodo_actual, resultado):
        """
        Método auxiliar para realizar el recorrido postorden de forma recursiva.

        Args:
            nodo_actual: El nodo actual en el proceso de recorrido.
            resultado: La lista que almacenará los valores del recorrido.

        Returns:
            La lista con los valores del recorrido postorden.
        """
        if nodo_actual:
            self._postorden_recursivo(nodo_actual.izquierda, resultado)
            self._postorden_recursivo(nodo_actual.derecha, resultado)
            resultado.append(nodo_actual.valor)
        return resultado

# Creación del árbol y adición de elementos
bst = ArbolDeBusquedaBinaria()
elementos = [50, 30, 20, 40, 70, 60, 80]

for e in elementos:
    bst.insertar(e)

print("Elementos insertados:", elementos)
# Realizar los recorridos y mostrar los resultados
print("Recorrido Preorden:", bst.preorden())
print("Recorrido Inorden:", bst.inorden())
print("Recorrido Postorden:", bst.postorden())