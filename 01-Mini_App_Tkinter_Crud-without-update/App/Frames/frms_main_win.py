from tkinter import *
from modules.crud import *

labels_input = ["descripcion","responsable","estado"]
labels_entry = []
tareas = []

#MARCOS
##Marco de formulario
def Frame_form(window: Tk, frm_data: Frame):
    frm_form = Frame(window)
    ##winfo mejor
    frm_form.config(width=window.winfo_width(),height=window.winfo_height()*0.20)
    frm_form.config(bg="light blue")
    frm_form.grid(row=0,column=0)
    
    labels_entry = crear_formulario(frm_form)
    
    i = 0
    for label_entry in labels_entry:
        label_entry["Label"].grid(row=i,column=0)
        label_entry["Entry"].grid(row=i,column=1)
        i += 1

    labels_entry[0]['Entry'].focus_set()
    
    submitBtn = Button(frm_form,text="Agregar",command= lambda: agregar_tarea(frm_data,tareas,labels_entry))
    submitBtn.grid(row=i,column=0)
    
    window.bind("<Return>", lambda e: agregar_tarea(frm_data,tareas,labels_entry))

##Marco de datos
def Frame_data(window: Tk):
    frm_data = Frame(window)
    frm_data.config(width=window.winfo_width(),height=window.winfo_height()*0.75)
    frm_data.grid(row=1, column=0, sticky='nsew')
    frm_data.config(bg="light gray")
    
    frm_data.columnconfigure(1,weight=2)
    frm_data.columnconfigure(2,weight=1)
    frm_data.columnconfigure(3,weight=1)
    
    Label(frm_data, text="ID", bg="light gray").grid(row=0,column=0)
    Label(frm_data, text=labels_input[0][0].upper()+labels_input[0][1:], width=50, bg="light gray").grid(row=0,column=1)
    i = 2
    for header in labels_input[1:]:
        Label(frm_data, text=header[0].upper()+header[1:], width=12, bg="light gray").grid(row=0,column=i)
        i += 1
    

    return frm_data

def get_tareas():
    return tareas