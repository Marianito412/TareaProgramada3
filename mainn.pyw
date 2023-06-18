#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 04/06/2023 12:25am
#Ultima version: 04/06/2023 1:30pm
#Version: 3.10.6

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import funciones
import archivos
import re
import funciones
from clases import Licencia


raiz = Tk()
raiz.title("COSEVI")
raiz.configure(bg="white")
raiz.resizable(False, False)
raiz.iconbitmap("Cosevi.ico")
raiz.geometry("650x600")

bg = PhotoImage(file = "fondo.png")
fondo = Canvas(raiz, width=650, height=600, bg="white")
fondo.pack()

bg = PhotoImage(file="fondo.png")
fondo.create_image(0, 0, image=bg, anchor="nw")

licencias = archivos.lee("Licencias")

def CrearLicencias():
    """
    Funcionalidad: Menú para crear una cantidad de personas e incluirlas en el padrón
    """
    Clicencias = tk.Toplevel()
    Clicencias.title("Crear licencias")
    Clicencias.configure(bg="white")
    Clicencias.iconbitmap("Cosevi.ico")
    Clicencias.resizable(False, False)
    Clicencias.geometry("400x400")
    Clicencias.grab_set()

    texto = Label(Clicencias, text="Crear licencias", bg="white", font=("Arial", 15))
    texto.place(x=130, y=30)

    textoPadron = Label(Clicencias,pady=15, text="¿A cuántos personas desea crear licencias?", bg="white", font=("Arial", 10),)
    textoPadron.place(x=70, y=80)


    FCantidad = Entry(Clicencias)

    BTCrear = Button(Clicencias, text="Generar",width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray", command=lambda: procesoLicencias(licencias, int(FCantidad.get())))
    BTCrear.configure(cursor="hand2")
    BTCrear.place(x=100, y=210)
    BTCrear.configure(state=tk.DISABLED)

    def limpiarDatos2():
        """
        Funcionalidad: Elimina los datos en el entry FCantidad
        """
        FCantidad.delete(0, tk.END)

    def activarBotonCrear(event):
        """
        Funcionalidad: Activa el boton crear si los datos en el entry FCantidad cumplen los requisitos
        Entradas:
        -event: se recorre la funcion cada vez que hay un cambio
        """
        if re.match('^\d{1,3}$', FCantidad.get()):
            if int(FCantidad.get())>250:
                etiquetaPadron.config(text="El número debe ser menor a 250",fg="gray")
                BTCrear.configure(state=tk.DISABLED)
            elif int(FCantidad.get())<1:
                etiquetaPadron.config(text="El número debe ser mayor a 0",fg="gray")
                BTCrear.configure(state=tk.DISABLED)
            else:
                BTCrear.configure(state=tk.NORMAL)
                etiquetaPadron.config(text="")
        else:
            etiquetaPadron.config(text="Debe digitar un número",fg="gray")
            BTCrear.configure(state=tk.DISABLED)

    etiquetaPadron=Label(Clicencias,bg="white")
    etiquetaPadron.place(x=140, y=160)
    
    FCantidad.bind("<KeyRelease>", activarBotonCrear)
    
    FCantidad.place(x=140, y=140)

    def procesoLicencias(padron,pNumero):
        """
        Funcionalidad: Manda a la funcion de crear padron y muestra un messagebox
        Entradas:
        -pPadron: padron de personas
        -pNumero: numero de personas a agregar
        """
        funciones.crearLicencias(licencias, int(pNumero))
        messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
        limpiarDatos2()

    bLimpiar = Button(Clicencias, text="Limpiar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=limpiarDatos2)
    bLimpiar.configure(cursor="hand2")
    bLimpiar.place(x=170, y=210)

    bRegresar = Button(Clicencias, text="Regresar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=Clicencias.destroy)
    bRegresar.configure(cursor="hand2")
    bRegresar.place(x=240, y=210)
        
def Renovar():
    """
    Funcionalidad: Menú para crear una cantidad de personas e incluirlas en el padrón
    """
    CRenovar = tk.Toplevel()
    CRenovar.title("Renovar licencias")
    CRenovar.configure(bg="white")
    CRenovar.iconbitmap("Cosevi.ico")
    CRenovar.resizable(False, False)
    CRenovar.geometry("400x400")
    CRenovar.grab_set()

    texto = Label(CRenovar, text="Renovar licencia", bg="white", font=("Arial", 15))
    texto.place(x=130, y=30)

    textoCedula = Label(CRenovar,pady=15, text="Cedula: ", bg="white", font=("Arial", 10),)
    textoCedula.place(x=35, y=80)


    FCedula = Entry(CRenovar)

    BTRenovar = Button(CRenovar, text="Renovar",width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray", command=lambda: procesoRenovarLicencias(licencias, FCedula.get()))
    BTRenovar.configure(cursor="hand2")
    BTRenovar.place(x=100, y=210)
    BTRenovar.configure(state=tk.DISABLED)

    def limpiarDatos2():
        """
        Funcionalidad: Elimina los datos en el entry FCantidad
        """
        FCedula.delete(0, tk.END)

    def validarCedula(pCedula):
        """
        Funcionalidad: valida una cédula contra regex
        Entradas:
        -pCedula(str): la cedula a validar
        Salidas:
        -pCedula: la cédula si cumple con las validaciones
        """
        if re.match(r"^\d{1}-\d{4}-\d{4}$", pCedula):
            return True
        else:
            return False


    def activarBotonCrear(event):
        """
        Funcionalidad: Activa el boton crear si los datos en el entry FCantidad cumplen los requisitos
        Entradas:
        -event: se recorre la funcion cada vez que hay un cambio
        """
        cedulas = [persona.mostrarCedula() for persona in licencias]
        print (cedulas)
        if not validarCedula(FCedula.get()):
            etiquetaCedula.config(text="Formato: 0-0000-0000",fg="gray")
            BTRenovar.configure(state=tk.DISABLED)

        elif not FCedula.get() in cedulas:
                etiquetaCedula.config(text="La cedula no existe",fg="gray")
        else:
            BTRenovar.configure(state=tk.NORMAL)
            etiquetaCedula.config(text="")

    etiquetaCedula=Label(CRenovar,bg="white")
    etiquetaCedula.place(x=135, y=125)
    
    FCedula.bind("<KeyRelease>", activarBotonCrear)
    
    FCedula.place(x=140, y=95)

    def procesoRenovarLicencias(licencias,pNumero):
        """
        Funcionalidad: Manda a la funcion de crear padron y muestra un messagebox
        Entradas:
        -pPadron: padron de personas
        -pNumero: numero de personas a agregar
        """
        funciones.renovarLicencias(licencias, FCedula.get())
        messagebox.showinfo(title="Verificacion",message="Se ha renovado con exito")
        limpiarDatos2()

    bLimpiar = Button(CRenovar, text="Limpiar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=limpiarDatos2)
    bLimpiar.configure(cursor="hand2")
    bLimpiar.place(x=170, y=210)

    bRegresar = Button(CRenovar, text="Regresar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=CRenovar.destroy)
    bRegresar.configure(cursor="hand2")
    bRegresar.place(x=240, y=210)

def generarPDF():
    """
    Funcionalidad: Menú para crear una cantidad de personas e incluirlas en el padrón
    """
    CPDF = tk.Toplevel()
    CPDF.title("Generar PDF")
    CPDF.configure(bg="white")
    CPDF.iconbitmap("Cosevi.ico")
    CPDF.resizable(False, False)
    CPDF.geometry("400x400")
    CPDF.grab_set()

    texto = Label(CPDF, text="Renovar licencia", bg="white", font=("Arial", 15))
    texto.place(x=130, y=30)

    textoCedula = Label(CPDF,pady=15, text="Cedula: ", bg="white", font=("Arial", 10),)
    textoCedula.place(x=20, y=80)


    FCantidad = Entry(CPDF)

    BTCrear = Button(CPDF, text="Renovar",width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray", command=lambda: procesoLicencias(padron, int(FCantidad.get())))
    BTCrear.configure(cursor="hand2")
    BTCrear.place(x=100, y=210)
    BTCrear.configure(state=tk.DISABLED)

    def limpiarDatos2():
        """
        Funcionalidad: Elimina los datos en el entry FCantidad
        """
        FCantidad.delete(0, tk.END)

    def activarBotonCrear(event):
        """
        Funcionalidad: Activa el boton crear si los datos en el entry FCantidad cumplen los requisitos
        Entradas:
        -event: se recorre la funcion cada vez que hay un cambio
        """
        if re.match('^\d{1,3}$', FCantidad.get()):
            if int(FCantidad.get())>250:
                etiquetaPadron.config(text="El número debe ser menor a 250",fg="gray")
                BTCrear.configure(state=tk.DISABLED)
            elif int(FCantidad.get())<1:
                etiquetaPadron.config(text="El número debe ser mayor a 0",fg="gray")
                BTCrear.configure(state=tk.DISABLED)
            else:
                BTCrear.configure(state=tk.NORMAL)
                etiquetaPadron.config(text="")
        else:
            etiquetaPadron.config(text="Debe digitar un número",fg="gray")
            BTCrear.configure(state=tk.DISABLED)

    etiquetaPadron=Label(CPDF,bg="white")
    etiquetaPadron.place(x=100, y=160)
    
    FCantidad.bind("<KeyRelease>", activarBotonCrear)
    
    FCantidad.place(x=140, y=80)

    def procesoLicencias(padron,pNumero):
        """
        Funcionalidad: Manda a la funcion de crear padron y muestra un messagebox
        Entradas:
        -pPadron: padron de personas
        -pNumero: numero de personas a agregar
        """
        funciones.CrearLicencias(padron, int(pNumero))
        messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
        limpiarDatos2()

    bLimpiar = Button(CPDF, text="Limpiar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=limpiarDatos2)
    bLimpiar.configure(cursor="hand2")
    bLimpiar.place(x=170, y=210)

    bRegresar = Button(CPDF, text="Regresar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=CPDF.destroy)
    bRegresar.configure(cursor="hand2")
    bRegresar.place(x=240, y=210)
   
def menuReportes():
    CReportes = tk.Toplevel()
    CReportes.title("Reportes")
    CReportes.configure(bg="white")
    CReportes.iconbitmap("Cosevi.ico")
    CReportes.resizable(False, False)
    CReportes.geometry("650x600")
    CReportes.grab_set()

    texto = Label(CReportes, text="Renovar licencia", bg="white", font=("Arial", 15))
    texto.place(x=130, y=30)

    bTotalLic = Button(CReportes, text="Totalidad de licencias", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
    bTotalLic.configure(cursor="hand2")
    bTotalLic.place(x=130, y=120)

    bTipoLic = Button(CReportes, text="Por tipo de licencia", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=OpcionCrearLicencias)
    bTipoLic.configure(cursor="hand2")
    bTipoLic.place(x=340, y=120)

    bExamenSan = Button(CReportes, text="Examen por sanción", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=Renovar)
    bExamenSan.configure(cursor="hand2")
    bExamenSan.place(x=130, y=220)

    bDonantes = Button(CReportes, text="Donantes de órganos", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=generarPDF)
    bDonantes.configure(cursor="hand2")
    bDonantes.place(x=340, y=220)

    bLicAnulada = Button(CReportes, text="Licencia anulada", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
    bLicAnulada.configure(cursor="hand2")
    bLicAnulada.place(x=130, y=320)

    bLicSede = Button(CReportes, text="Licencias por sede", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
    bLicSede.configure(cursor="hand2")
    bLicSede.place(x=340, y=320)

    bSalir = Button(CReportes, text="Salir", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=salirPrograma)
    bSalir.configure(cursor="hand2")
    bSalir.place(x=240, y=420)
    

def salirPrograma():
    messagebox.showinfo(title="COSEVI",message="No olvides gestionar pronto tu licencia")
    raiz.destroy()
    

#Ventana principal

bXML = Button(raiz, text="Crear XML", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
bXML.configure(cursor="hand2")
bXML.place(x=130, y=120)

bLicencias = Button(raiz, text="Crear licencias", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=OpcionCrearLicencias)
bLicencias.configure(cursor="hand2")
bLicencias.place(x=340, y=120)

bRenovar = Button(raiz, text="Renovar licencias", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=Renovar)
bRenovar.configure(cursor="hand2")
bRenovar.place(x=130, y=220)

bPDF = Button(raiz, text="Generar PDF", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=generarPDF)
bPDF.configure(cursor="hand2")
bPDF.place(x=340, y=220)

bExcel = Button(raiz, text="Reportes de Excel", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=menuReportes)
bExcel.configure(cursor="hand2")
bExcel.place(x=130, y=320)

bAcerca = Button(raiz, text="Acerca de", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
bAcerca.configure(cursor="hand2")
bAcerca.place(x=340, y=320)

bSalir = Button(raiz, text="Salir", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=salirPrograma)
bSalir.configure(cursor="hand2")
bSalir.place(x=240, y=420)



