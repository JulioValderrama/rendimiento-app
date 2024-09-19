import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk  # Para crear pestañas

# Funciones de análisis
def convertir_fecha(df):
    df['Fecha'] = pd.to_datetime(df['Fecha'], format='%d/%m/%Y')
    df['Año'] = df['Fecha'].dt.year
    df['Mes'] = df['Fecha'].dt.month_name()
    return df

def calcular_media_segun_objetivo_entrenamiento(df, media_deseada, objetivo=None, tipo_entrenamiento=None):
    df_filtrado = df
    if objetivo:
        df_filtrado = df_filtrado[df_filtrado['Objetivo del Entrenamiento'] == objetivo]
    if tipo_entrenamiento:
        df_filtrado = df_filtrado[df_filtrado['Tipo de Entrenamiento'] == tipo_entrenamiento]
    if df_filtrado.empty:
        print("No se encontraron datos.")
        return None
    return df_filtrado[media_deseada].mean()

def calcular_distancia_total(df, modalidad, año=None, mes=None):
    df_filtrado = df[df['Modalidad de Entrenamiento'] == modalidad]
    if año:
        df_filtrado = df_filtrado[df_filtrado['Fecha'].dt.year == int(año)]
    if mes:
        df_filtrado = df_filtrado[df_filtrado['Fecha'].dt.month_name() == mes]
    if df_filtrado.empty:
        print("No se encontraron datos.")
        return None
    distancia_total = df_filtrado['Distancia Total (m)'].sum()
    return distancia_total

def relacionar_dos_variables(df, variable1, variable2):
    sns.jointplot(x=variable1, y=variable2, data=df)
    plt.show()

# Funciones de interfaz
def analizar_media():
    objetivo = combo_objetivo.get()
    modalidad = combo_modalidad.get()
    year = combo_anio.get()
    month = combo_mes.get()
    media_deseada = combo_media.get()
    resultado = calcular_media_segun_objetivo_entrenamiento(df, media_deseada, objetivo, modalidad)
    if resultado:
        lbl_resultado.config(text=f"Resultado: {resultado:.2f}")

def analizar_distancia():
    modalidad = combo_modalidad.get()
    year = combo_anio.get()
    month = combo_mes.get()
    resultado = calcular_distancia_total(df, modalidad, year, month)
    if resultado:
        lbl_resultado.config(text=f"Resultado: {resultado:.2f} metros")

def analizar_relacion():
    variable1 = combo_variable1.get()
    variable2 = combo_variable2.get()
    relacionar_dos_variables(df, variable1, variable2)

# Cargar los datos y preparar el DataFrame
ruta_csv = 'data/data.csv'
df = pd.read_csv(ruta_csv)
df = convertir_fecha(df)

# Crear la ventana principal
root = Tk()
root.title("Análisis de Datos Deportivos")

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
notebook.add(frame_analisis, text="Análisis")
notebook.add(frame_relacion, text="Relación de Variables")

# Opciones para los combos
opciones_objetivo = df['Objetivo del Entrenamiento'].unique().tolist()
opciones_modalidad = df['Modalidad de Entrenamiento'].unique().tolist()
opciones_anio = df['Año'].unique().tolist()
opciones_mes = df['Mes'].unique().tolist()
opciones_media = df.columns.tolist()  # Todas las columnas para seleccionar la media
opciones_variables = df.columns.tolist()  # Todas las columnas para comparar

# Desplegables para análisis
Label(frame_analisis, text="Objetivo del Entrenamiento").pack()
combo_objetivo = ttk.Combobox(frame_analisis, values=opciones_objetivo)
combo_objetivo.pack()

Label(frame_analisis, text="Modalidad de Entrenamiento").pack()
combo_modalidad = ttk.Combobox(frame_analisis, values=opciones_modalidad)
combo_modalidad.pack()

Label(frame_analisis, text="Año").pack()
combo_anio = ttk.Combobox(frame_analisis, values=opciones_anio)
combo_anio.pack()

Label(frame_analisis, text="Mes").pack()
combo_mes = ttk.Combobox(frame_analisis, values=opciones_mes)
combo_mes.pack()

Label(frame_analisis, text="Columna de Media").pack()
combo_media = ttk.Combobox(frame_analisis, values=opciones_media)
combo_media.pack()

# Botón para analizar la media o distancia
Button(frame_analisis, text="Analizar Media", command=analizar_media).pack(pady=5)
Button(frame_analisis, text="Analizar Distancia", command=analizar_distancia).pack(pady=5)

# Resultado de análisis
lbl_resultado = Label(frame_analisis, text="Resultado: ")
lbl_resultado.pack(pady=10)

# Desplegables para relación entre dos variables
Label(frame_relacion, text="Variable 1").pack()
combo_variable1 = ttk.Combobox(frame_relacion, values=opciones_variables)
combo_variable1.pack()

Label(frame_relacion, text="Variable 2").pack()
combo_variable2 = ttk.Combobox(frame_relacion, values=opciones_variables)
combo_variable2.pack()

# Botón para analizar la relación
Button(frame_relacion, text="Analizar Relación", command=analizar_relacion).pack(pady=5)

# Ejecutar la ventana principal
root.mainloop()
