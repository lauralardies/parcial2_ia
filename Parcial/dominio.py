# Importamos bibliotecas
import numpy as np

def creacion_dominio(x, y, z):
    """
    Crea un arreglo tridimensional de ceros con las dimensiones especificadas.

    Parámetros:
        x (int): Número de elementos en la dirección x.
        y (int): Número de elementos en la dirección y.
        z (int): Número de elementos en la dirección z.

    Devuelve:
        dominio (ndarray): Arreglo tridimensional de ceros con las dimensiones especificadas.
    """
    
    # Crea un arreglo tridimensional de ceros con las dimensiones especificadas
    dominio = np.zeros((x, y, z))

    return dominio

# Ejemplo de uso
dominio = creacion_dominio(10, 10, 10)

# Mostramos el arreglo tridimensional
print(dominio)