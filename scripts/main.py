import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Para el Treeview
import pandas as pd

# Función para abrir el diálogo de selección de archivo y cargar el CSV
def importar_csv():
    # Abrir el cuadro de diálogo para seleccionar el archivo
    ruta_archivo = filedialog.askopenfilename(
        title = "Seleccionar archivo CSV",
        filetypes = (("CSV files", "*.csv"), ("All files", "*.*"))
    )

    if ruta_archivo:  # Verifica que se haya seleccionado un archivo
        try:
            # Leer el CSV y crear el DataFrame
            df = pd.read_csv(ruta_archivo)
            # Mostrar el DataFrame en la consola (para fines de depuración)
            print(df)
            # Llamar a la función que muestra el DataFrame en la interfaz
            mostrar_dataframe(df)
        except Exception as e:
            messagebox.showerror("Error", f"Error al abrir el archivo\n{e}")

# Función para mostrar el DataFrame en formato de tabla
def mostrar_dataframe(df):
    # Limpiar el área de visualización si ya había contenido
    for widget in area_mostrar.winfo_children():
        widget.destroy()
    
    # Crear el Treeview
    tabla = ttk.Treeview(area_mostrar)
    
    # Definir las columnas
    tabla["columns"] = list(df.columns)
    tabla["show"] = "headings"  # Solo mostrar los encabezados, sin columna extra a la izquierda

    # Configurar los encabezados de columna
    for col in tabla["columns"]:
        tabla.heading(col, text=col)  # Encabezado de la columna
        tabla.column(col, anchor="center")  # Alineación del contenido
    
    # Insertar los datos fila por fila
    for index, row in df.iterrows():
        tabla.insert("", "end", values=list(row))
    
    # Empacar el Treeview en el frame de visualización
    tabla.pack(fill="both", expand=True)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("App de Análisis del Rendimiento")

# Menú desplegable
menubar = tk.Menu(ventana)
ventana.config(menu=menubar)

# Añadir opción de "Archivo" al menú
archivo_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Archivo", menu=archivo_menu)
archivo_menu.add_command(label="Importar CSV", command=importar_csv)

# Añadir área para mostrar el DataFrame
area_mostrar = tk.Frame(ventana)
area_mostrar.pack(pady=20, fill="both", expand=True)

# Ejecutar la ventana
ventana.mainloop()