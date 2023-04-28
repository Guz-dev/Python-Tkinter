from tkinter import *
from tkinter import messagebox

from Frames.frms_main_win import *
#from Frames.frms_sec_win import *

#TESTING DEVELOPING BRANCH
WIDTH = 1000
HEIGHT = 600
#VENTANAS
##Ventana principal
def Main_window():
    main_win = Tk()
    main_win.title("Ventana Principal")
    main_win.geometry(f"{WIDTH}x{HEIGHT}+0+0")
    main_win.resizable(False,False)

    frm_data = Frame_data(main_win)
    Frame_form(main_win,frm_data)
    #Frame_form(main_win,frm_data, lambda: Secondary_window(main_win,tareas))
    

    #Secondary_window(main_win)    
    main_win.mainloop()
    
""" 
##Ventana secundaria
def Secondary_window(main_win: Tk, tareas: list):
    sec_win = Toplevel(main_win)
    sec_win.title("Editar dato")
    sec_win.geometry(f"{int(WIDTH/2)}x{HEIGHT}+{WIDTH}+0")

    sec_win.config(bg="light blue")

    Frame_edit(sec_win, tareas)
    
    sec_win.mainloop()
""" 

if __name__ == "__main__":
    Main_window()

    
#EDITAR EN NUEVA VENTANA y DESPUES CONTENIDO PRUEBA 