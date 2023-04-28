from tkinter import *
from modules.crud import *
""" 
labels_input = ["descripcion","responsable","estado"]

def Frame_edit(sec_win: Toplevel,tareas: list, index: int):
    labels_entry = crear_formulario(sec_win,15)

    i = 0
    for label_entry in labels_entry:
        label_entry["Label"].grid(row=i,column=0,padx=sec_win.winfo_reqwidth() - 120, pady=20)
        label_entry["Entry"].grid(row=i+1,column=0,padx=sec_win.winfo_reqwidth() - 120)

        i += 2

    labels_entry[0]['Entry'].focus_set()
    
    editBtn = Button(sec_win,text="Editar",command= lambda: editar(sec_win, tareas, labels_entry,index), font=('Arial','14'))
    editBtn.grid(row=i,column=0,pady=10)
    
    sec_win.bind("<Return>", lambda e: editar(sec_win,tareas,labels_entry,index))
 """