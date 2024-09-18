import pandas as pd
import matplotlib.pyplot as plt

# Función para cargar datos desde un CSV
def cargar_datos(ruta_csv):
    df = pd.read_csv(ruta_csv)
    return df

# Función para calcular la distancia total por modalidad
def calcular_distancia_total_por_modalidad(df):
    distancia_total = df.groupby('Modalidad de Entrenamiento')['Distancia Total (m)'].sum()
    return distancia_total

# Función para generar el gráfico de la distancia total por modalidad
def graficar_distancias_por_modalidad(distancias):
    # Crear un gráfico de barras con las modalidades y las distancias totales
    distancias.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])

    plt.title('Distancia Total Recorrida por Modalidad de Entrenamiento')
    plt.xlabel('Modalidad')
    plt.ylabel('Distancia Total (m)')
    plt.grid(True)
    plt.show()

# Ejecución principal
if __name__ == '__main__':
    # Ruta al archivo CSV
    ruta_csv = 'data/Entradas.csv'

    # Cargar los datos
    df = cargar_datos(ruta_csv)
    df.info()

    # Calcular las distancias totales por modalidad
    distancias_totales = calcular_distancia_total_por_modalidad(df)

    # Generar el gráfico
    graficar_distancias_por_modalidad(distancias_totales)
