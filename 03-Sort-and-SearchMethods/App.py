"""
ENUNCIADO

1 -> Menu con botones

2 -> ¿Que tiene el menu?

    * Agregar persona
    * Eliminar persona
    * Listar personas
    
    * Listar ordenadamente -> Insertion Sort o Bubble Sort o Selection Sort
    
    * Buscar persona -> Busqueda binaria o secuencial/lineal
    
    **Que muestre paso a paso el algoritmo de ordenamiento o busqueda**
"""

from tkinter import * 
from funciones_menu import *
from CONSTANTS import ENTRIES



#¿Qué necesitas para pedir los datos en tkinter? de:

#Agregar Persona -> 3 Label y Entry (nombre, fecha de nacimiento, rut) y un boton de agregar
#Eliminar Persona -> 1 Label y Entry (rut) y un boton de eliminar
#Listar Personas -> varios Label para mostrar la lista de personas

#Listar ordenadamente -> varios Label para mostrar la lista de personas

#Buscar persona -> 1 Label y Entry (rut) y un boton de buscar

def Frame_Agregar_Persona(sec_win: Toplevel):
    persona = {}
    
    frame_agregar_persona = Frame(sec_win, bg="lightblue", width=400, height=600)
    
    for entry in ENTRIES:       
        Label(frame_agregar_persona, text=entry, width=20).grid(row=ENTRIES.index(entry), column=0)
        persona[entry] = Entry(frame_agregar_persona, name=entry, width=20)
        persona[entry].grid(row=ENTRIES.index(entry), column=1)
    
    submitBtn = Button(frame_agregar_persona, text="Agregar", command=lambda:(agregar_persona(persona,personas)))
    submitBtn.grid(row=len(ENTRIES), column=0, columnspan=2)
    
    return frame_agregar_persona

def Frame_Eliminar_Persona(sec_win: Toplevel):
    frame_eliminar_persona = Frame(sec_win, bg="lightblue", width=400, height=600)

    rut_entry = Entry(frame_eliminar_persona, width=20)
    rut_entry.grid(row=0, column=1)

    submitBtn = Button(frame_eliminar_persona, text="Eliminar", command=lambda: eliminar_persona(rut_entry.get(), personas))
    submitBtn.grid(row=1, column=0, columnspan=2)

    return frame_eliminar_persona

def Frame_Listar_Personas(sec_win: Toplevel):
    frame_listar_personas = Frame(sec_win, bg="lightblue", width=400, height=600)

    listbox = Listbox(frame_listar_personas, width=65)
    listbox.grid(row=0, column=0)

    for persona in personas:
        listbox.insert(END, f"{persona}: {personas[persona]}")

    return frame_listar_personas

def Sec_win(type_win: str):
    sec_win = Toplevel()
    
    sec_win.geometry("400x600+800+0")
    sec_win.title("Sec Menu")
    sec_win.config(bg="lightblue")
    
    print(type_win)
    try:
        if type_win == "agregar":
            frm_win = Frame_Agregar_Persona(sec_win)
        elif type_win == "eliminar":
            frm_win = Frame_Eliminar_Persona(sec_win)
        elif type_win == "listar":
            frm_win = Frame_Listar_Personas(sec_win)            
        elif type_win == "listar_ordenadamente":
            pass
        elif type_win == "buscar":
            pass
        
        frm_win.pack()
    except:
        messagebox.showerror("Error", "No se ha encontrado la ventana")
        sec_win.destroy()
        
    sec_win.mainloop()
    return sec_win

def Main_Win():
    main_win = Tk()
    main_win.geometry("800x800+0+0")
    main_win.title("Menu")
    main_win.config(bg="lightblue")
    
    btnAdd = Button(main_win, text="Agregar persona", name="agregar" , command=lambda:(Sec_win(btnAdd.winfo_name())))
    btnAdd.pack()

    btnDel = Button(main_win, text="Eliminar persona", name="eliminar" , command=lambda:(Sec_win(btnDel.winfo_name())))
    btnDel.pack()
    
    btnList = Button(main_win, text="Listar personas", name="listar" , command=lambda:(Sec_win(btnList.winfo_name())))
    btnList.pack()

    return main_win

personas = {}

if __name__ == '__main__':    
    main_win = Main_Win()

    main_win.mainloop()