from tkinter import *

""" 
    Create Read Update     Delete (CRUD)
    Crear  Leer Actualizar Eliminar
"""
labels_input = ["descripcion","responsable","estado"]

def crear_formulario(wid: Widget, width: int = 30):
    """ Funcion que nos genera un arreglo de pares Etiqueta y Entrada [[Label,Entry],...]"""
    labels_entry = []    
    for label in labels_input:
        labels_entry.append({
            "Label": Label(wid,text=label,width=width, bg="light blue",font=('Arial','14')),
            "Entry": Entry(wid,width=width*2,font=('Arial','14'))
        })
        
    return labels_entry

#CREATE
def agregar_tarea(wid_data: Widget,tareas: list,formulario: list):
    print("Entro a agregar")
    tarea = {}
    tarea['id'] = len(tareas) + 1
    for entrada in formulario:
        tarea[entrada["Label"].cget("text")] = entrada["Entry"].get()

    tarea["Eliminar"] = Button(wid_data,text="Eliminar",command=lambda: eliminar_tarea(wid_data,tareas,tarea["Eliminar"].grid_info()['row']),width=10)
    #tarea["Editar"] = Button(wid_data,text="Editar",command=lambda: editar_tarea(wid_data,tareas,tarea["Editar"].grid_info()['row']),width=10)
    tareas.append(tarea)
    
    formulario[0]["Entry"].focus_set()
    for entrada in formulario:
        entrada["Entry"].delete(0,END)
        
    actualizar_tareas(wid_data,tareas)

#READ
def actualizar_tareas(wid_data: Widget, tareas: list):
    for i in range(len(tareas)):
        Label(wid_data,text=str(tareas[i]['id']), bg="light gray").grid(row=i+1,column=0)
        j = 1
        for label in labels_input:
            Label(wid_data,text=tareas[i][label], bg="light gray").grid(row=i+1,column=j)
            j += 1
        tareas[i]["Eliminar"].grid(row=i+1,column=j,pady=5,padx=5)
        #tareas[i]["Editar"].grid(row=i+1,column=j+1,pady=5,padx=5)

#UPDATE
""" 
def editar_tarea(wid_data: Widget, tareas: list, index: int, Sec_win):
    Sec_win(wid_data.winfo_toplevel(),tareas,index)
    
def editar(wid_data: Widget, tareas: list, formulario: list, index: int):
    print("Entro a editar")
    tarea = {}
    tarea['id'] = len(tareas) + 1
    for entrada in formulario:
        tarea[entrada["Label"].cget("text")] = entrada["Entry"].get()

    tareas.append(tarea)
    
    formulario[0]["Entry"].focus_set()
    for entrada in formulario:
        entrada["Entry"].delete(0,END)
        
    actualizar_tareas(wid_data,tareas)
"""
 
#DELETE
def eliminar_tarea(wid_data: Widget, tareas: list, index: int):
    #print(index)
    #print(f"El id es : {tareas[index-1]['id']}")
    
    widgets = wid_data.grid_slaves(row=index)
    for widget in widgets:
        widget.destroy()

    # Get a list of all the widgets in the grid
    widgets = wid_data.grid_slaves()

    # Iterate over the widgets and move them to new positions in the grid
    for widget in widgets:
        info = widget.grid_info()
        row = info['row']
        column = info['column']
        if row > index:
            widget.grid_forget()
            widget.grid(row=row-1, column=column,pady=5,padx=5)

    tareas.pop(index-1)

