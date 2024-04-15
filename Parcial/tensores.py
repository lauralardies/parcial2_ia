import numpy as np

def tensor_deformacion(desplazamientos):
    """
    Calcula el tensor de deformaciones para un elemento finito tetraédrico
    dada su matriz de desplazamientos nodales.

    Parámetros:
        desplazamientos (array_like): Matriz de desplazamientos nodales.
            Debe ser una matriz de forma (4, 3), donde cada fila representa
            los desplazamientos en un nodo (x, y, z).

    Devuelve:
        tensor_deformacion (ndarray): Tensor de deformaciones.
            Es una matriz 3x3 simétrica que representa las deformaciones
            en el elemento finito.

    Nota:
        Esta función es un ejemplo simplificado y utiliza np.gradient() para calcular
        el gradiente de los desplazamientos. Dependiendo de tu aplicación específica
        y de cómo estén estructurados tus datos, es posible que necesites implementar
        el cálculo del gradiente de manera diferente.
    """

    return np.gradient(desplazamientos)

# Ejemplo de uso
desplazamientos = np.array([[1.0, 2.0, 3.0],
                            [2.0, 3.0, 4.0],
                            [3.0, 4.0, 5.0],
                            [4.0, 5.0, 6.0]])
tensor = tensor_deformacion(desplazamientos)
print("Tensor de deformaciones:")
print(tensor)