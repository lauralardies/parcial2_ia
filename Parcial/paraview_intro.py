# Importamos bibliotecas
import pandas as pd

# Generamos un dataframe de pandas con los datos de un análisis estructural
df = pd.DataFrame({'x': [0, 1], 'y': [0, 1], 'z': [0, 1], 'presion': [100, 150]})

# Exportamos el dataframe a un archivo CSV
df.to_csv('output.csv', index=False)

'''
¿Cómo visualizar estos resultados en Paraview?
Para visualizar los resultados en Paraview, primero debemos inicializa Paraview en nuestro sistema.
Luego, abrimos el archivo CSV que exportamos en el paso anterior (output.csv) en Paraview.
Elegimos el tipo de datos, nosotros seleccionamos "Table" ya que estamos importando datos tabulares.
Una vez que los datos se han importado, podemos visualizarlos en Paraview utilizando diferentes tipos 
de gráficos y representaciones a elección del usuario.
'''