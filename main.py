
import webbrowser
import re
from tkinter import END, Frame, Scrollbar, filedialog, messagebox, ttk
import tkinter
import os
import easygui
from Analizador import Analizador
class main:
    def __init__(self,root) -> None:
        self.ventana=root
        self.ventana.title("Analizador léxico")
        self.ventana.configure(bg="white")
        logo =".\Icono\icono.ico" 
        self.ventana.iconbitmap(logo)
        self.ventana.resizable(0,0)
        self.gadgets()
    
    def gadgets(self):
        self.Frame=Frame()
        self.Frame.pack()
        self.Frame.config(bg="NavajoWhite4")
        self.Frame.config(width="800",height="600")

        frame=Frame()
        frame.place(x=225,y=60)
        scrollbar=Scrollbar(frame)
        scrollbar.pack(side="right",fill="y")
        
        self.MostrarTxt=tkinter.Text(frame,width="65", height="30", yscrollcommand=scrollbar.set)
        self.MostrarTxt.pack(side="left")

        scrollbar.config(command=self.MostrarTxt.yview)

        Boton_abrirArchivo= tkinter.Button(self.Frame,text="Abrir archivo",font=("bold",13),bg="white", command=self.Abrir_Archivo)
        Boton_abrirArchivo.place(x=25,y=60)

        Boton_Guardar= tkinter.Button(self.Frame,text="Guardar",font=("bold",13),bg="white",command=self.Guardar)
        Boton_Guardar.place(x=25,y=110)

        Boton_GuardarComo= tkinter.Button(self.Frame,text="Guardar como",font=("bold",13),bg="white", command=self.Guardar_como)
        Boton_GuardarComo.place(x=25,y=160)

        Boton_Analizar= tkinter.Button(self.Frame,text="Analizar",font=("bold",13),bg="white",
        command=self.analizar)
        Boton_Analizar.place(x=25,y=210)

        Boton_Errores= tkinter.Button(self.Frame,text="Errores",font=("bold",13),bg="white",
        command=self.Abrir_Html_Errores)
        Boton_Errores.place(x=25,y=260)

        Boton_Salir= tkinter.Button(self.Frame,text="Salir",font=("bold",13),bg="red",foreground="white",
        command=self.Salir)
        Boton_Salir.place(x=25,y=500)

        Boton_abrirDocumento= tkinter.Button(self.Frame,text="Abrir",font=("bold",13),bg="white", command=self.B_Ayuda)
        Boton_abrirDocumento.place(x=75,y=360)

        self.Boton_Ayuda= ttk.Combobox(self.Frame,font=("bold",13),state="readonly",
        values=["Manual de usuario","Manual técnico","Autor"],justify='center')
        self.Boton_Ayuda.place(x=10,y=325)
        self.Boton_Ayuda.current(2)
    def Salir (self):
        self.ventana.destroy()
    def Abrir_Archivo(self):
        self.ruta = easygui.fileopenbox(title="Abre el archivo .txt")
        try:
            archivo= open(self.ruta,'r',encoding='utf-8')
            contenido=archivo.read()
            archivo.close()
        except:
            print("ERROR primer try")
        try:
            self.MostrarTxt.delete("1.0",END)
            self.MostrarTxt.insert(END,contenido)
        except:
            print("ERROR")
    def analizar(self):
        contenido= str(self.MostrarTxt.get("1.0",END))
        if contenido!="":

            Analizador(contenido).compile()
            self.Abrir_Html_Resultados()

    def Guardar(self):
        contenido= str(self.MostrarTxt.get("1.0",END))
        if contenido!="":
            try:
                direccion= self.ruta
                ruta= open(direccion,'w')
                ruta.write(contenido)
                ruta.close()
                
                print("INFO GUARDADA")
            except:
                messagebox.showinfo(title="Atención",message="No se han guardado los cambios")

    def Guardar_como(self,file_path=None):
        contenido= str(self.MostrarTxt.get("1.0",END))      
        if contenido!="":
            if file_path is None:
                try:
                    file_path = filedialog.asksaveasfilename(
                        filetypes=(("Archivos de texto", "*.txt"),("Todos los archivos", "*.*")))
                    ruta= open(file_path,'w')
                    ruta.write(contenido)
                    ruta.close()
                except:
                    print("ERROR")

    def B_Ayuda(self):
        eleccion= self.Boton_Ayuda.get()
        if eleccion=="Manual de usuario":
            webbrowser.open_new_tab("file:///"+os.getcwd()+"/Manuales/Manual de Usuario.pdf")
        elif eleccion=="Autor":
             webbrowser.open_new_tab("file:///"+os.getcwd()+"/Manuales/Autor.pdf")
        elif eleccion=="Manual técnico":
             webbrowser.open_new_tab("file:///"+os.getcwd()+"/Manuales/Manual técnico.pdf")

    def Abrir_Html_Errores(self):
        print(os.getcwd())
        if os.path.exists("./Records/ERRORES_201902363.html"):
           webbrowser.open_new_tab("file:///"+os.getcwd()+"/Records/ERRORES_201902363.html")
        else:
            messagebox.showinfo(title="Atención",message="No se ha encontrado el archivo")
    def Abrir_Html_Resultados(self):
        if os.path.exists("./Records/RESULTADOS_201902363.html"):
            webbrowser.open_new_tab("file:///"+os.getcwd()+"/Records/RESULTADOS_201902363.html")
        else:
            messagebox.showinfo(title="Atención",message="No se ha encontrado el archivo")


           


root=tkinter.Tk()
Ventana=main(root)
root.mainloop()