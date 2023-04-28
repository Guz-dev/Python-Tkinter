""" ESTRUCTURA DE DATOS diccionario de diccionarios 
personas: { 
    rut: {
        nombre: ,
        fecha_nacimiento: 
        }
    }
"""
from tkinter import messagebox, END
from mis_funciones.busqueda_lineal_y_binaria import *
from CONSTANTS import ENTRIES  #[nombre, fecha_nacimiento, rut]
import re

def agregar_persona(persona: dict,personas: dict): #es una idea no ma, no es la original
    rut = persona["rut"].get()
    try:
        rut = rut[:-1] + rut[-1].upper()
    except:
        pass
    
    print(rut)
    if not re.match(r'^\d{1,2}\.\d{3}\.\d{3}[-][0-9K]{1}$', rut):
        return messagebox.showerror("Error", "El rut no es valido")

    nombre = persona["nombre"].get()
    nombre = nombre[0].upper() + nombre[1:].lower()
    
    fecha_nacimiento = persona["fecha_nacimiento"].get()
    if not re.match(r'^\d{1,2}\/\d{1,2}\/\d{4}$', fecha_nacimiento):
        return messagebox.showerror("Error", "La fecha no es valida")
        
    personas[rut] = {"nombre": nombre, "fecha_nacimiento": fecha_nacimiento}

    for entry in persona:
        persona[entry].delete(0, END)
    persona["rut"].focus()

def eliminar_persona(rut: str, personas: dict):
    if busqueda_binaria(rut, list(personas.keys())) > len(personas):
        return messagebox.showerror("Error", "El rut no existe")
    
    confirm = messagebox.askyesno("Confirmar", f"¿Estas seguro de eliminar a la persona con rut {rut}?")
    if confirm:
        personas.pop(rut, None)
        
        return messagebox.showinfo("Eliminado", f"La persona con rut {rut} ha sido eliminada")