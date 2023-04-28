import tkinter as tk            #Importa el módulo "tkinter" y lo renombra como "tk" para utilizar widgets y funciones de la biblioteca.
from tkinter import messagebox  #Proporciona ventanas de mensajes emergentes.

tareas = []          #Define una lista vacia que se utilizará para almacenar las tareas que serán ingresadas.

CANT_MAX_TAREAS = 11 #Limita la cantidad máxima de tareas que se agregarán a la lista.

#La función sirve para agregar nuevas tareas y en caso de que alcanzara el límite, entonces muestra un mensaje de error.
def agregar_tarea():                                                      #Función para agregar nuevas tareas a una lista
    if len(tareas) == CANT_MAX_TAREAS:                                    #Comprobar la cantidad de tareas almacenadas en "tareas" sea igual a la cantidad máxima
        messagebox.showerror("Error", "No se pueden agregar mas campos!") #Al alcanzar la cantidad máxima de tareas, acá se muestra un mensaje de error
        return                                                            #El módulo "messagebox" hace que devuelva el None con la clave "return"

    if not descripcion or not responsable or not estado:                       #El if comprueba si las variables son una cadena vacía.
        messagebox.showerror("Error", "Todos los campos deben estar llenos")   #Si el campo está vacío, se muestra un mensaje de error.
        return                                                                 #Interrumpe la ejecución del código.
    
    descripcion = descripcion_entry.get()   #Las tareas que se almacenan son menores que la cantidad máxima de tareas, la función
    responsable = responsable_entry.get()   #continuará y se obtendrá aquella descripción utilizando las variables.
    estado = estado_entry.get()             #Get() obtienen y limpian los datos que se ingresan.

    tareas.append({"descripcion": descripcion, "responsable": responsable, "estado": estado}) #La tarea se agrega a un nuevo diccionario con las claves y variables.
    actualizar_tabla()                                                                        #Actualiza la tabla que muestra las tareas.


def eliminar_tarea():                                                        #Función que elimina una tarea seleccionada en la lista.
    indice_seleccionado = tabla_tareas.curselection()                        #Se obtiene el índice de la tarea seleccionada.
    if not indice_seleccionado:                                              #Comprobación si se seleccionó una tarea.
        messagebox.showerror("Error", "Seleccione una tarea para eliminar")  #Muestra mensaje de error en caso de no seleccionarse alguna tarea.
        return                                                               #Interrumpe la ejecución de la función.

    tareas.pop(indice_seleccionado[0])  #Elimina una tarea de la lista con la función "curselection()" obteniendo el índice.
    actualizar_tabla()                  #Llama la función para actualizar la tabla con las tareas ingresadas.

def actualizar_tabla():                       #Función que actualiza la tabla que muestra las tareas ingresadas.
    tabla_tareas.delete(0, tk.END)            #Borra las filas, desde la fila 0 hasta el final de la tabla.
    for index, tarea in enumerate(tareas):    #El "for" recorre la lista y utiliza la función "enumerate()" para obtener el índice.
        #Inserta una nueva fila a la tabla.
        tabla_tareas.insert(tk.END, f"{index+1}. {tarea['descripcion']}             ({tarea['responsable']}):            {tarea['estado']}")

ventana = tk.Tk()                           #Creación de nueva ventana utilizando módulo Tkinter.
ventana.title("Gestión de Tareas")          #Título de la ventana utilizada.

ventana.config(bg="light gray")             #Color de fondo de la ventana principal.

ventana.geometry("800x400")                 #Establece las dimensiones de la ventana.

ventana.resizable(width=False,height=False) #Establece que la ventana no se puede redimensionar.

#Widgets:
descripcion_label = tk.Label(ventana, text="Descripción:", bg= "Light Green", font=("Verdana", 10, "italic"), width=12) #Etiqueta que muestra el texto "Descripción" en la ventana.
descripcion_entry = tk.Entry(ventana, bg = "Light Green",width=70)                                                      #Entrada en la ventana para ingresar una descripción.
responsable_label = tk.Label(ventana, text="Responsable:", bg= "Light Blue", font=("Verdana", 10, "italic"), width=12)  #Etiqueta que muestra el texto "Responsable" en la ventana.
responsable_entry = tk.Entry(ventana, bg = "Light Blue",width=50)                                                       #Entrada en la ventana para ingresar un nombre del responsable.
estado_label = tk.Label(ventana, text="Estado:", bg= "Yellow", font=("Verdana", 10, "italic"), width=12)                #Etiqueta que muestra el texto "Estado" en la ventana.
estado_entry = tk.Entry(ventana, bg = "Yellow",width=30)                                                                #Entrada en la ventana para ingresar el estado de la tarea.
tabla_label = tk.Label(ventana, text= "Descripción\t\tResponsable\t\tTarea")                                            #Muestra el encabezado de una tabla en la ventana.

boton_agregar = tk.Button(ventana, text="Agregar tarea", command=agregar_tarea)    #La función "agregar_tarea" se ejecutará al presionar.
boton_eliminar = tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea) #La función "eliminar_tarea" se ejecutará al presionar.
tabla_tareas = tk.Listbox(ventana, width=100,height=17,font=('Arial','14'))        #Lista desplegable que se crea dentro de la ventana.

#El "grid" posiciona y dimensiona widgets.
#row=fila  /   column= columna

#Se posicionan los widgets utilizando grid en sus respectivas filas y columnas
descripcion_label.grid(row=0, column=0, sticky="w")
descripcion_entry.grid(row=0, column=1, sticky="w")
responsable_label.grid(row=1, column=0, sticky="w")
responsable_entry.grid(row=1, column=1, sticky="w")
estado_label.grid(row=2, column=0, sticky="w")
estado_entry.grid(row=2, column=1, sticky="w")

boton_agregar.grid(row=3, column=0, sticky="w")                  #Posiciona botón agregar y lo alinea.
boton_eliminar.grid(row=3, column=1, sticky="w")                 #Posiciona botón eliminar y lo alinea.
tabla_label.grid(row=4, column=0, columnspan=2, pady=(10, 0))    #Posiciona etiqueta y agrega espacio entre la fila y la tabla de tareas.
tabla_tareas.grid(row=5, column=0, columnspan=10, pady=(10, 0))  #Posiciona caja de lista y agrega espacio entre tabla de encabezado y la lista de tareas.

#Muestra la ventana.
ventana.mainloop()
    