import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt  # Importar matplotlib para mostrar los gráficos
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
from tkinter import *
from tkinter import ttk  # Para crear pestañas

# Convertir 'Fecha' a formato datetime
def convertir_fecha(df):
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
    df['Año'] = df['Fecha'].dt.year  # Extraer el año
    df['Mes'] = df['Fecha'].dt.month_name()  # Extraer el nombre del mes
    return df

# Función para calcular la media según el objetivo del entrenamiento
def calcular_media_segun_objetivo_entrenamiento(df, media_deseada, objetivo=None, tipo_entrenamiento=None):
    # Filtrar por objetivo si se proporciona
    if objetivo:
        df_filtrado = df[df['Objetivo del Entrenamiento'] == objetivo]
    
    # Filtrar por tipo de entrenamiento si se proporciona
    if tipo_entrenamiento:
        df_filtrado = df_filtrado[df_filtrado['Tipo de Entrenamiento'] == tipo_entrenamiento]
    
    # Verificar si el DataFrame resultante no está vacío
    if df_filtrado.empty:
        print("No se encontraron datos para los filtros especificados.")
        return None
    
    # Calcular y retornar la media
    return df_filtrado[media_deseada].mean()

# Función para calcular la distancia total
def calcular_distancia_total(df, modalidad, objetivo=None, año=None, mes=None):
    # Filtrar por modalidad de entrenamiento
    df_filtrado = df[df['Modalidad de Entrenamiento'] == modalidad]

    # Filtrar por objetivo si se proporciona
    if objetivo:
        df_filtrado = df_filtrado[df_filtrado['Objetivo del Entrenamiento'] == objetivo]

    # Filtrar por año si se proporciona
    if año:
        df_filtrado = df_filtrado[df_filtrado['Fecha'].dt.year == int(año)]
    
    # Filtrar por mes si se proporciona
    if mes:
        df_filtrado = df_filtrado[df_filtrado['Fecha'].dt.month_name() == mes]

    # Verificar si el DataFrame resultante está vacío
    if df_filtrado.empty:
        print("No se encontraron datos para los filtros especificados.")
        return None
    
    # Calcular la suma de la columna 'Distancia Total (m)'
    distancia_total = df_filtrado['Distancia Total (m)'].sum()

    return distancia_total

def relacionar_dos_variables(df, variable1, variable2):
    # Verificar si el DataFrame resultante está vacío
    if df.empty:
        print("No se encontraron datos para los filtros especificados.")
        return None
    # Verificar si se entrega dos variables
    elif not variable1 or not variable2:
        print('Por favor, introduce dos variables')
        return None
    
    # Mostrar gráfico para la comparativa
    sns.jointplot(x=variable1, y=variable2, data=df)
    plt.show()

# -------------------------------------------------------Funciones de interfaz -------------------------------------------------------

def analizar_distancia():
    modalidad = combo_modalidad_entrenamiento.get()
    objetivo = combo_obetivo_entrenamiento.get()
    año = combo_año.get()
    mes = combo_mes.get()
    distancia_total = calcular_distancia_total(df, modalidad, objetivo, año, mes)

    if distancia_total == None:
        label_resultado_analisis.config(text=f'No se encontraron datos para los filtros especificados')

    label_resultado_analisis.config(text=distancia_total)
    


# Ruta del archivo CSV (ajusta según tu caso)
ruta_csv = 'data/data.csv'

# Cargar los datos
df = pd.read_csv(ruta_csv)

# Convertir la columna 'Fecha' a datetime y extraer año y mes
df = convertir_fecha(df)


# Crear la ventana principal
root = Tk()
root.title("Análisis del Rendimiento")

# Crear el Notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Crear el primer Frame para el análisis
frame_analisis = Frame(notebook, width=400, height=400)
frame_analisis.pack(fill="both", expand=True)

# Crear el segundo Frame para la relación entre dos variables
frame_relacion = Frame(notebook, width=400, height=400)
frame_relacion.pack(fill="both", expand=True)

# Añadir los Frames como pestañas en el Notebook
notebook.add(frame_analisis, text='Análisis')
notebook.add(frame_relacion, text='Relación')

# Opciones para los combos
opciones_modalidad = [''] + df['Modalidad de Entrenamiento'].unique().tolist()
opciones_objetivo = [''] + df['Objetivo del Entrenamiento'].unique().tolist()
opciones_año = [''] + df['Año'].unique().tolist()
opciones_mes = [''] + df['Mes'].unique().tolist()

# Desplegables para análisis
Label(frame_analisis, text='Modalidad de Entrenamiento', pady=5, font=("Arial", 10, "bold")).pack()
combo_modalidad_entrenamiento = ttk.Combobox(frame_analisis, values=opciones_modalidad, justify='center')
combo_modalidad_entrenamiento.pack()

Label(frame_analisis, text='Objetivo del Entrenamiento', pady=5, font=("Arial", 10, "bold")).pack()
combo_obetivo_entrenamiento = ttk.Combobox(frame_analisis, values=opciones_objetivo, justify='center')
combo_obetivo_entrenamiento.pack()

Label(frame_analisis, text='Año', pady=5, font=("Arial", 10, "bold")).pack()
combo_año = ttk.Combobox(frame_analisis, values=opciones_año, justify='center')
combo_año.pack()

Label(frame_analisis, text='Mes', pady=5, font=("Arial", 10, "bold")).pack()
combo_mes = ttk.Combobox(frame_analisis, values=opciones_mes, justify='center')
combo_mes.pack()

# Botón para analizar la media o distancia
Button(frame_analisis, text='Analizar Distancia', command=analizar_distancia).pack(pady=10)

# Resultado de análisis
Label(frame_analisis, text='RESULTADO', pady=20).pack()
label_resultado_analisis = Label(frame_analisis, text='Resultado AQUI', font=("Arial", 12, "bold"), anchor='center')
label_resultado_analisis.pack()


# Ejecutar la ventana principal
root.mainloop()


