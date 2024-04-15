# Importamos bibliotecas
import pandas as pd

def generar_y_exportar_csv(x, y, z, presion, nombre_archivo):
    """
    Genera un DataFrame de Pandas con los datos proporcionados y lo exporta a un archivo CSV.

    Parámetros:
        x (list): Lista de coordenadas x.
        y (list): Lista de coordenadas y.
        z (list): Lista de coordenadas z.
        presion (list): Lista de valores de presión.
        nombre_archivo (str): El nombre del archivo CSV de salida.
    """

    # Generamos un DataFrame de Pandas con los datos proporcionados
    df = pd.DataFrame({'x': x, 'y': y, 'z': z, 'presion': presion})

    # Exportamos el DataFrame a un archivo CSV
    df.to_csv(nombre_archivo, index=False)

# Ejemplo de uso
x = [0, 1]
y = [0, 1]
z = [0, 1]
presion = [100, 150]
nombre_archivo = 'output.csv'
generar_y_exportar_csv(x, y, z, presion, nombre_archivo)

'''
¿Cómo visualizar estos resultados en Paraview?
Para visualizar los resultados en Paraview, primero debemos inicializa Paraview en nuestro sistema.
Luego, abrimos el archivo CSV que exportamos en el paso anterior (output.csv) en Paraview.
Elegimos el tipo de datos, nosotros seleccionamos "Table" ya que estamos importando datos tabulares.
Una vez que los datos se han importado, podemos visualizarlos en Paraview utilizando diferentes tipos 
de gráficos y representaciones a elección del usuario.
'''