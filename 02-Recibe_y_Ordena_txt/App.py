from mis_funciones.busqueda_lineal_y_binaria import *
from mis_funciones.metodos_ordenamiento import *

from tkinter import *
from tkinter import filedialog
import pathlib

arrays_list = []

def open_file(uploadBtn,fileDownloadBtn):   
    file_uploaded = filedialog.askopenfilename(initialdir = pathlib.Path, title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    
    try:
        file = open(file_uploaded,"r")
        
        
        for line in file:
            arrays_list.append(line.replace(" ","").replace("[","").replace("]","").replace('"',"").replace("'","").split()[0].split(","))
            
        for array_index in range(len(arrays_list)):
            arr_int = []
            try:
                for i in arrays_list[array_index]:
                    arr_int.append(int(i))
                arrays_list[array_index] = arr_int
            except:            
                continue
            
        for array in arrays_list:
            insertion_sort(array)
        
        fileDownloadBtn.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        uploadBtn.destroy()
    except:
        print("Error: No se pudo abrir el archivo 'mis_arreglos_sin_orden.txt'")    
    
def download_file(main_win):
    
    download_path = filedialog.asksaveasfilename(initialdir = pathlib.Path, title = "Select file", filetypes = (("txt files","*.txt"),("all files","*.*")))
    
    if download_path:
        new_file = open(download_path+".txt","w")
        
        for array in arrays_list:
            new_file.write(str(array)+"\n")
        
        new_file.close()
    
    main_win.destroy()
    

def Main_window():
    main_win = Tk()
    main_win.geometry("400x400+500+200")
    main_win.title("Ordenamiento y búsqueda de arreglos")

    main_win.resizable(False, False)
    
    uploadBtn = Button(main_win, text="Subir archivo para ordenar", command=lambda: open_file(uploadBtn,fileDownloadBtn))
    uploadBtn.place(relx=0.5, rely=0.4, anchor=CENTER)

    fileDownloadBtn = Button(main_win, text="Descargar archivo ordenado", command=lambda: download_file(main_win))
    
    
    return main_win


if __name__ == "__main__":
    main_win = Main_window() # Create the main window
    main_win.mainloop() # Start the main loop
    

## ARRAYS QUE CONTENGAN 2 O MÁS ELEMENTOS REPETIDOS USANDO BUSQUEDA BINARIA O LINEAL