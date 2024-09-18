import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd

# Crear clase principal para la aplicación
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Entrenamiento")
        self.root.geometry("800x600")
        
        # Crear el menú principal
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menú con opciones para cambiar entre los diferentes frames
        menu_secciones = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Secciones", menu=menu_secciones)
        menu_secciones.add_command(label="Dashboard", command=self.mostrar_dashboard)
        menu_secciones.add_command(label="Entradas", command=self.mostrar_entradas)
        menu_secciones.add_command(label="Análisis", command=self.mostrar_analisis)

        # Inicializar los frames
        self.frame_actual = None
        self.frame_dashboard = None
        self.frame_entradas = None
        self.frame_analisis = None

        # Inicializar la app mostrando el dashboard
        self.mostrar_dashboard()

    # Función para cambiar los frames (pestañas)
    def cambiar_frame(self, frame):
        if self.frame_actual is not None:
            self.frame_actual.pack_forget()  # Esconde el frame actual
        self.frame_actual = frame
        self.frame_actual.pack(fill="both", expand=True)

    # Función para mostrar el dashboard
    def mostrar_dashboard(self):
        if self.frame_dashboard is None:
            self.frame_dashboard = tk.Frame(self.root)
            label = tk.Label(self.frame_dashboard, text="Dashboard - Aquí irán los gráficos", font=("Helvetica", 16))
            label.pack(pady=20)
        self.cambiar_frame(self.frame_dashboard)

    # Función para mostrar la ventana de entradas (con tabla)
    def mostrar_entradas(self):
        if self.frame_entradas is None:
            self.frame_entradas = tk.Frame(self.root)
            label = tk.Label(self.frame_entradas, text="Entradas de Entrenamiento", font=("Helvetica", 16))
            label.pack(pady=20)
            
            # Treeview para mostrar la tabla
            self.tree = ttk.Treeview(self.frame_entradas, columns=("Fecha", "Año", "Mes", "Hora", "Modalidad", "Categoría",
                                                                   "Tipo", "Objetivo", "Distancia", "Tiempo", "Paladas", 
                                                                   "Ritmo 500m", "Ritmo km", "Velocidad", "FC Recomendada", 
                                                                   "FC Media", "Calorias", "Sueño", "Ayuno", "Café", "Comentarios"),
                                     show="headings")
            
            # Configurar las columnas
            columnas = ["Fecha", "Año", "Mes", "Hora", "Modalidad", "Categoría", "Tipo", "Objetivo", "Distancia", "Tiempo", 
                        "Paladas", "Ritmo 500m", "Ritmo km", "Velocidad", "FC Recomendada", "FC Media", "Calorias", "Sueño", 
                        "Ayuno", "Café", "Comentarios"]
            
            for col in columnas:
                self.tree.heading(col, text=col)
                self.tree.column(col, anchor="center", width=100)
            
            self.tree.pack(fill="both", expand=True)
            
            # Botón para importar CSV
            boton_importar = tk.Button(self.frame_entradas, text="Importar CSV", command=self.importar_csv)
            boton_importar.pack(pady=10)

        self.cambiar_frame(self.frame_entradas)

    # Función para mostrar la ventana de análisis
    def mostrar_analisis(self):
        if self.frame_analisis is None:
            self.frame_analisis = tk.Frame(self.root)
            label = tk.Label(self.frame_analisis, text="Análisis - Selecciona variables y periodo", font=("Helvetica", 16))
            label.pack(pady=20)
            
            # Variables de análisis
            label_variable = tk.Label(self.frame_analisis, text="Seleccione la variable a analizar:")
            label_variable.pack(pady=5)
            variable_analisis = ttk.Combobox(self.frame_analisis, values=["Distancia", "Tiempo", "Ritmo", "Velocidad"])
            variable_analisis.pack(pady=5)
            
            label_periodo = tk.Label(self.frame_analisis, text="Seleccione el periodo de análisis:")
            label_periodo.pack(pady=5)
            periodo_analisis = ttk.Combobox(self.frame_analisis, values=["Última semana", "Último mes", "Último año"])
            periodo_analisis.pack(pady=5)
            
            boton_analizar = tk.Button(self.frame_analisis, text="Analizar", command=lambda: self.analizar(variable_analisis.get(), periodo_analisis.get()))
            boton_analizar.pack(pady=10)
            
        self.cambiar_frame(self.frame_analisis)

    # Función para importar CSV y llenar la tabla
    def importar_csv(self):
        ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo CSV", filetypes=(("CSV files", "*.csv"), ("Todos los archivos", "*.*")))
        if ruta_archivo:
            try:
                df = pd.read_csv(ruta_archivo)
                self.tree.delete(*self.tree.get_children())  # Limpiar tabla
                for _, row in df.iterrows():
                    self.tree.insert("", "end", values=list(row))
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo importar el archivo: {e}")

    # Función para realizar análisis (simulada)
    def analizar(self, variable, periodo):
        if not variable or not periodo:
            messagebox.showwarning("Advertencia", "Seleccione una variable y un periodo.")
        else:
            messagebox.showinfo("Análisis", f"Analizando {variable} para el periodo {periodo}.")

# Configuración de la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
