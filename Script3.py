import matplotlib.pyplot as plt
import numpy as np

# Definimos los valores de x
x = np.linspace(-10, 10, 100)

# Definimos la función sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Calculamos los valores de y usando la función sigmoide
y = sigmoid(x)

# Creamos la gráfica
plt.plot(x, y)

# Añadimos un título y etiquetas a los ejes
plt.title("Gráfica de la función sigmoide")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
