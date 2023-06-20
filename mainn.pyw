#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 04/06/2023 12:25am
#Ultima version: 19/06/2023 1:30pm
#Version: 3.10.6

#Importación de bibliotecas
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import archivos
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
archivos.graba("Licencias", licencias)

flagReporteTotal= True
flagDonantes= True
flagTipoLic= True
flagReporteSancion=True
flagLicAnulada= True
flagReporteSedeCentral= True
flagReporteSedeAlajuela= True
flagReporteSedeCartago= True
flagReporteSedeHeredia= True
flagReporteSedeSanRamon= True
flagReporteSedeSanCarlos = True
flagReporteSedeGuapiles= True
flagReporteSedeLimon= True
flagReporteSedeLiberia= True
flagReporteSedeNicoya= True
flagReporteSedePuntarenas= True
flagReporteSedePerezZeledon= True
flagReporteSedeGolfito= True

#Definición de funciones
ba = PhotoImage() 
def opcionCrearLicencias():
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

    global ba
    ba.configure(file = "Crearlicencias.png")
    ba1 = Canvas(Clicencias, width=400, height=400, bg="white")
    ba1.pack()

    ba1.create_image(0, 0, image=ba, anchor="nw")


    textoPadron = Label(Clicencias,pady=15, text="¿A cuántos personas desea crear licencias?", bg="white", font=("Arial", 10),)
    textoPadron.place(x=70, y=100)

    FCantidad = Entry(Clicencias)

    BTCrear = Button(Clicencias, text="Generar",width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray", command=lambda: procesoLicencias(licencias, int(FCantidad.get())))
    BTCrear.configure(cursor="hand2")
    BTCrear.place(x=100, y=240)
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
    etiquetaPadron.place(x=140, y=190)
    
    FCantidad.bind("<KeyRelease>", activarBotonCrear)
    
    FCantidad.place(x=140, y=160)

    def procesoLicencias(padron,pNumero):
        """
        Funcionalidad: Manda a la funcion de crear padron y muestra un messagebox
        Entradas:
        -pPadron: padron de personas
        -pNumero: numero de personas a agregar
        """
        funciones.crearLicencias(licencias, int(pNumero))
        archivos.graba("Licencias", licencias)
        messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
        limpiarDatos2()

    bLimpiar = Button(Clicencias, text="Limpiar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=limpiarDatos2)
    bLimpiar.configure(cursor="hand2")
    bLimpiar.place(x=170, y=240)

    bRegresar = Button(Clicencias, text="Regresar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=Clicencias.destroy)
    bRegresar.configure(cursor="hand2")
    bRegresar.place(x=240, y=240)

def opcionCrearXML():
    """
    Funcionalidad: Generar XML y conseguir los tipos de licencias
    """
    funciones.conseguirTipoLicencias()
    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")

be = PhotoImage()

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

    global be
    be.configure(file = "Renovarlicencias.png")
    be1 = Canvas(CRenovar, width=400, height=400, bg="white")
    be1.pack()

    be1.create_image(0, 0, image=be, anchor="nw")

    textoCedula = Label(CRenovar,pady=15, text="Cedula: ", bg="white", font=("Arial", 10),)
    textoCedula.place(x=40, y=120)

    FCedula = Entry(CRenovar)

    BTRenovar = Button(CRenovar, text="Renovar",width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray", command=lambda: procesoRenovarLicencias(licencias, FCedula.get()))
    BTRenovar.configure(cursor="hand2")
    BTRenovar.place(x=100, y=230)
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
        if not validarCedula(FCedula.get()):
            etiquetaCedula.config(text="Formato: 0-0000-0000",fg="gray")
            BTRenovar.configure(state=tk.DISABLED)

        elif not FCedula.get() in cedulas:
                etiquetaCedula.config(text="La cedula no existe",fg="gray")
        else:
            BTRenovar.configure(state=tk.NORMAL)
            etiquetaCedula.config(text="")

    etiquetaCedula=Label(CRenovar,bg="white")
    etiquetaCedula.place(x=135, y=175)
    
    FCedula.bind("<KeyRelease>", activarBotonCrear)
    
    FCedula.place(x=140, y=135)

    def procesoRenovarLicencias(licencias,pNumero):
        """
        Funcionalidad: Manda a la funcion de crear padron y muestra un messagebox
        Entradas:
        -pPadron: padron de personas
        -pNumero: numero de personas a agregar
        """
        for persona in licencias:
                if persona.mostrarCedula()==FCedula.get():
                    if persona.mostrarPuntaje()== 0:
                        archivos.graba("Licencias", licencias)
                        messagebox.showwarning(title="Verificacion",message="No se puede renovar porque su puntaje es 0")
                        limpiarDatos2()
                    else:
                        funciones.renovarLicencias(licencias, FCedula.get())
                        archivos.graba("Licencias", licencias)
                        messagebox.showinfo(title="Verificacion",message="Se ha renovado con exito")
                        limpiarDatos2()

    bLimpiar = Button(CRenovar, text="Limpiar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=limpiarDatos2)
    bLimpiar.configure(cursor="hand2")
    bLimpiar.place(x=170, y=230)

    bRegresar = Button(CRenovar, text="Regresar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=CRenovar.destroy)
    bRegresar.configure(cursor="hand2")
    bRegresar.place(x=240, y=230)

bi = PhotoImage()

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

    global bi
    bi.configure(file = "generarPDF.png")
    bi1 = Canvas(CPDF, width=400, height=400, bg="white")
    bi1.pack()

    bi1.create_image(0, 0, image=bi, anchor="nw")

    textoCedula = Label(CPDF,pady=15, text="Cedula: ", bg="white", font=("Arial", 10),)
    textoCedula.place(x=40, y=120)


    FCedula = Entry(CPDF)

    BTCrear = Button(CPDF, text="Generar",width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray", command=lambda: procesoPDF(licencias, FCedula.get()))
    BTCrear.configure(cursor="hand2")
    BTCrear.place(x=100, y=230)
    BTCrear.configure(state=tk.DISABLED)

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

    def limpiarDatos2():
        """
        Funcionalidad: Elimina los datos en el entry FCantidad
        """
        FCedula.delete(0, tk.END)

    def activarBotonCrear(event):
        """
        Funcionalidad: Activa el boton crear si los datos en el entry FCantidad cumplen los requisitos
        Entradas:
        -event: se recorre la funcion cada vez que hay un cambio
        """
        cedulas = [persona.mostrarCedula() for persona in licencias]
        if not validarCedula(FCedula.get()):
            etiquetaCedula.config(text="Formato: 0-0000-0000",fg="gray")
            BTCrear.configure(state=tk.DISABLED)

        elif not FCedula.get() in cedulas:
                etiquetaCedula.config(text="La cedula no existe",fg="gray")
        else:
            BTCrear.configure(state=tk.NORMAL)
            etiquetaCedula.config(text="")

    etiquetaCedula=Label(CPDF,bg="white")
    etiquetaCedula.place(x=135, y=175)
    
    FCedula.bind("<KeyRelease>", activarBotonCrear)
    
    FCedula.place(x=140, y=135)

    def procesoPDF(padron,pNumero):
        """
        Funcionalidad: Manda a la funcion de crear padron y muestra un messagebox
        Entradas:
        -pPadron: padron de personas
        -pNumero: numero de personas a agregar
        """
        resultado = funciones.generarPDF(licencias, FCedula.get())
        messagebox.showinfo(title="Verificacion",message="Se ha creado con exito"if resultado else "No se encontró a la persona")
        limpiarDatos2()

    bLimpiar = Button(CPDF, text="Limpiar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=limpiarDatos2)
    bLimpiar.configure(cursor="hand2")
    bLimpiar.place(x=170, y=230)

    bRegresar = Button(CPDF, text="Regresar", width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray",command=CPDF.destroy)
    bRegresar.configure(cursor="hand2")
    bRegresar.place(x=240, y=230)

bs = PhotoImage()

def opcionReporteTipoLicencias():
    """
    Funcionalidad: Generar el reporte por tipo de licencia
    """
    CReporteTipo = tk.Toplevel()
    CReporteTipo.title("Reporte por tipo de licencia")
    CReporteTipo.configure(bg="white")
    CReporteTipo.iconbitmap("Cosevi.ico")
    CReporteTipo.resizable(False, False)
    CReporteTipo.geometry("450x400")
    CReporteTipo.grab_set()

    global bs
    bs.configure(file = "reporteTipo.png")
    bs1 = Canvas(CReporteTipo, width=450, height=400, bg="white")
    bs1.pack()
    bs1.create_image(0, 0, image=bs, anchor="nw")

    def activarGenerar(event):
        """
        Funcionalidad: Activa el boton de generar reporte
        """
        BTCrear.configure(state=tk.NORMAL)

    def procesoReporte():
        """
        Funcionalidad: Genera el reporte de tipo licencia
        """
        funciones.reporteTipoLicencia(licencias, cajaOpciones.get())
        messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")

    texto = Label(CReporteTipo, text="Seleccione la opcion con el tipo de licencia a consultar", bg="white", font=("Arial", 10))
    texto.place(x=70, y=110)

    cajaOpciones = ttk.Combobox(CReporteTipo,width=30, values=funciones.conseguirTipoLicencias())
    cajaOpciones.place(x=130, y=170)
    cajaOpciones.bind("<<ComboboxSelected>>", activarGenerar)

    BTCrear = Button(CReporteTipo, text="Generar",width=8, height=1, font=("Arial", 8), activebackground="lightpink",bg="lightgray", command=procesoReporte)
    BTCrear.configure(cursor="hand2")
    BTCrear.place(x=205, y=230)
    BTCrear.configure(state=tk.DISABLED)

def opcionExamenPorSancion():
    """
    Funcionalidad: Genera el reporte de personas con sanción
    """
    global flagReporteSancion
    if flagReporteSancion==True:
        funciones.reporteSancion(licencias)
        messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
    else:
        messagebox.showinfo(title="Verificacion",message="El documento ya existe")
    flagReporteSancion=False

def opcionReporteTotal():
    """
    Funcionalidad: genera el reporte con la totalidad de la BD
    """
    global flagReporteTotal
    if flagReporteTotal==True:
        funciones.reporteTotal(licencias)
        messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
    else:
        messagebox.showinfo(title="Verificacion",message="El documento ya existe")
    flagReporteTotal=False

bo = PhotoImage()
bu = PhotoImage()

def menuReportes():
    """
    Funcionalidad: Muestra en menú de reportes
    """
    CReportes = tk.Toplevel()
    CReportes.title("Reportes")
    CReportes.configure(bg="white")
    CReportes.iconbitmap("Cosevi.ico")
    CReportes.resizable(False, False)
    CReportes.geometry("500x600")
    CReportes.grab_set()

    global bo
    bo.configure(file = "Reportes.png")
    bo1 = Canvas(CReportes, width=500, height=600, bg="white")
    bo1.pack()
    bo1.create_image(0, 0, image=bo, anchor="nw")

    def procesoDonantes():
        """
        Funcionalidad: Genera el reporte de donadores
        """
        global flagDonantes
        if flagDonantes==True:
            funciones.reporteDonador(licencias)
            messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
        else:
            messagebox.showinfo(title="Verificacion",message="El documento ya existe")
        flagDonantes=False
        
    def procesoTipoLic():
        global flagTipoLic
        if flagTipoLic==True:
            funciones.reporteTipoLicencia(licencias)
            messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
        else:
            messagebox.showinfo(title="Verificacion",message="El documento ya existe")
        flagTipoLic=False

    def procesoLicAnulada():
        """
        Funcionalidad: Genera el reporte de anulados
        """
        global flagLicAnulada
        if flagLicAnulada==True:
            funciones.reporteAnulado(licencias)
            messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
        else:
            messagebox.showinfo(title="Verificacion",message="El documento ya existe")
        flagLicAnulada=False

    def reporteLicSede():
        """
        Funcionalidad: Muestar un menú para poder solicitar un reporte de una sede específica
        """
        def procesoReporteSedeCentral():
            """
            Funcionalidad: Genera el reporte de los anulados
            """
            global flagReporteSedeCentral
            if flagReporteSedeCentral==True:
                funciones.reporteAnulado(licencias)
                messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
            else:
                messagebox.showinfo(title="Verificacion",message="El documento ya existe")
            flagReporteSedeCentral=False
        
        def procesoLicSedes(pOpcion):
            """
            Funcionalidad: Genera el reporte de la sede seleccionada
            """
            print(pOpcion)

            if pOpcion=="Dirección General de Educación Vial licencias sede central":
                global flagReporteSedeCentral
                if flagReporteSedeCentral==True:
                    funciones.reporteSedeCentral(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeCentral=False
            elif pOpcion=="Dirección General de Educación Vial licencias Alajuela":
                global flagReporteSedeAlajuela
                if flagReporteSedeCentral==True:
                    funciones.reporteSedeAlajuela(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeAlajuela=False
            elif pOpcion=="Dirección General de Educación Vial licencias Cartago":
                global flagReporteSedeCartago
                if flagReporteSedeCartago==True:
                    funciones.reporteSedeCartago(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeCartago=False
            elif pOpcion=="Dirección General de Educación Vial licencias Heredia":
                global flagReporteSedeHeredia
                if flagReporteSedeHeredia==True:
                    funciones.reporteSedeHeredia(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeHeredia=False
            elif pOpcion=="Dirección General de Educación Vial licencias San Ramón":
                global flagReporteSedeSanRamon
                if flagReporteSedeSanRamon==True:
                    funciones.reporteSedeSanRamon(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeSanRamon=False
            elif pOpcion=="Dirección General de Educación Vial licencias Guápiles":
                global flagReporteSedeGuapiles
                if flagReporteSedeGuapiles==True:
                    funciones.reporteSedeGuapiles(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeGuapiles=False
            elif pOpcion=="Dirección General de Educación Vial licencias Limón":
                global flagReporteSedeLimon
                if flagReporteSedeLimon==True:
                    funciones.reporteSedeLimon(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeLimon=False
            elif pOpcion=="Dirección General de Educación Vial licencias Liberia":
                global flagReporteSedeLiberia
                if flagReporteSedeLiberia==True:
                    funciones.reporteSedeLiberia(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeLiberia=False
            elif pOpcion=="Dirección General de Educación Vial licencias Nicoya":
                global flagReporteSedeNicoya
                if flagReporteSedeNicoya==True:
                    funciones.reporteSedeNicoya(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeNicoya=False
            elif pOpcion=="Dirección General de Educación Vial licencias Puntarenas":
                global flagReporteSedePuntarenas
                if flagReporteSedePuntarenas==True:
                    funciones.reporteSedePuntarenas(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedePuntarenas=False
            elif pOpcion=="Dirección General de Educación Vial licencias Pérez Zeledón":
                global flagReporteSedePerezZeledon
                if flagReporteSedePerezZeledon==True:
                    funciones.reporteSedePerezZeledon(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedePerezZeledon=False
            elif pOpcion=="Dirección General de Educación Vial licencias Río Claro de Golfito":
                global flagReporteSedeGolfito
                if flagReporteSedeGolfito==True:
                    funciones.reporteSedeGolfito(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeGolfito=False
            elif pOpcion=="Dirección General de Educación Vial licencias San Carlos":
                global flagReporteSedeSanCarlos
                if flagReporteSedeSanCarlos==True:
                    funciones.reporteSedeSanCarlos(licencias)
                    messagebox.showinfo(title="Verificacion",message="Se ha creado con exito")
                else:
                    messagebox.showinfo(title="Verificacion",message="El documento ya existe")
                flagReporteSedeSanCarlos=False
                   
        def activarBotonSede(event):
            """
            Funcionalidad: Activa el botón para buscar solo si la sede a buscar no es vacía
            """
            if event.widget.get() != "":
                bConsultar.configure(state=tk.NORMAL)
            else:
                bConsultar.configure(state=tk.DISABLED)

        repSede = tk.Toplevel()
        repSede.title("Reporte por sede")
        repSede.configure(bg="white")
        repSede.resizable(True, True)
        repSede.grab_set()
        repSede.geometry("500x400")

        global bu
        bu.configure(file = "reporteSedes.png")
        bu1 = Canvas(repSede, width=500, height=600, bg="white")
        bu1.pack()
        bu1.create_image(0, 0, image=bu, anchor="nw")

        texto = Label(repSede, text="Seleccione la opcion con la sede a consultar", bg="white", font=("Arial", 10))
        texto.place(x=110, y=110)
        
        
        cajaOpciones= ttk.Combobox(repSede,width=60, values=["Dirección General de Educación Vial, licencias sede central", "Dirección General de Educación Vial licencias Alajuela",
                                                    "Dirección General de Educación Vial licencias Cartago", "Dirección General de Educación Vial licencias Heredia",
                                                    "Dirección General de Educación Vial licencias San Ramón", "Dirección General de Educación Vial licencias Guápiles",
                                                    "Dirección General de Educación Vial licencias Limón", "Dirección General de Educación Vial licencias Liberia",
                                                    "Dirección General de Educación Vial licencias Nicoya", "Dirección General de Educación Vial licencias Puntarenas",
                                                    "Dirección General de Educación Vial licencias Pérez Zeledón", "Dirección General de Educación Vial licencias Río Claro de Golfito",
                                                    "Dirección General de Educación Vial licencias San Carlos"])
        cajaOpciones.bind("<<ComboboxSelected>>", activarBotonSede)
        cajaOpciones.place(x=55, y=180)
        bConsultar = Button(repSede, text="Consultar", state=tk.DISABLED ,width=10, height=1, font=("Arial", 8), activebackground="#fbd404",bg="lightgray", command=lambda : procesoLicSedes(cajaOpciones.get()))
        bConsultar.place(x=210, y=245)

    def salirProgramaReportes():
        """
        Funcionalidad: Cierra el menú de reportes
        """
        CReportes.destroy()

    bTotalLic = Button(CReportes, text="Totalidad de licencias", width=18, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray", command=opcionReporteTotal)
    bTotalLic.configure(cursor="hand2")
    bTotalLic.place(x=70, y=130)

    bTipoLic = Button(CReportes, text="Por tipo de licencia", width=18, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=opcionReporteTipoLicencias)

    #bTipoLic = Button(CReportes, text="Por tipo de licencia", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=procesoTipoLic)

    bTipoLic.configure(cursor="hand2")
    bTipoLic.place(x=270, y=130)

    bExamenSan = Button(CReportes, text="Examen por sanción", width=18, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=opcionExamenPorSancion)
    bExamenSan.configure(cursor="hand2")
    bExamenSan.place(x=70, y=220)

    bDonantes = Button(CReportes, text="Donantes de órganos", width=18, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=procesoDonantes)
    bDonantes.configure(cursor="hand2")
    bDonantes.place(x=270, y=220)

    bLicAnulada = Button(CReportes, text="Licencia anulada", width=18, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=procesoLicAnulada)
    bLicAnulada.configure(cursor="hand2")
    bLicAnulada.place(x=70, y=320)

    bLicSede = Button(CReportes, text="Licencias por sede", width=18, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=reporteLicSede)
    bLicSede.configure(cursor="hand2")
    bLicSede.place(x=270, y=320)

    bSalir = Button(CReportes, text="Salir", width=18, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=salirProgramaReportes)
    bSalir.configure(cursor="hand2")
    bSalir.place(x=170, y=420)
    

def salirPrograma():
    """
    Funcionalidad: Cierra el programa
    """
    messagebox.showinfo(title="COSEVI",message="No olvides gestionar pronto tu licencia")
    raiz.destroy()
    

FMariano = PhotoImage()
FNicole = PhotoImage()
bc = PhotoImage() 
def acercaDe():
    """
    Funcionalidad: Muestra la información de los desarolladores
    """
    CAcercaDe = tk.Toplevel()
    CAcercaDe.title("Acerca De")
    CAcercaDe.configure(bg="white")
    CAcercaDe.iconbitmap("Cosevi.ico")
    CAcercaDe.resizable(False, False)
    CAcercaDe.geometry("500x500")
    CAcercaDe.grab_set()

    global bc
    bc.configure(file = "desarrolladores.png")
    bc1 = Canvas(CAcercaDe, width=500, height=500, bg="white")
    bc1.pack()

    bc1.create_image(0, 0, image=bc, anchor="nw")
    
    global FNicole
    FNicole.configure(file="nicole.png")
    #FMariano = PhotoImage()
    lNicole = Label(CAcercaDe, image=FNicole, width=100, height=100)
    lNicole.place(x=80, y=150)

    LNicole = Label(CAcercaDe, text="Nicole Parra", bg="white", font=("Arial", 11))
    LNicole.place(x=90, y=270)

    LNicole1 = Label(CAcercaDe, text="2023223291", bg="white", font=("Arial", 11))
    LNicole1.place(x=90, y=300)

    global FMariano
    FMariano.configure(file="marianoo.png")
    #FMariano = PhotoImage()
    lMariano = Label(CAcercaDe, image=FMariano, width=100, height=100)
    lMariano.place(x=320, y=150)

    LMariano = Label(CAcercaDe, text="Mariano Soto", bg="white", font=("Arial", 11))
    LMariano.place(x=325, y=270)

    LMariano1 = Label(CAcercaDe, text="2020142918", bg="white", font=("Arial", 11))
    LMariano1.place(x=325, y=300)

#Ventana principal

bXML = Button(raiz, text="Crear XML", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray", command=opcionCrearXML)
bXML.configure(cursor="hand2")
bXML.place(x=130, y=120)

bLicencias = Button(raiz, text="Crear licencias", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=opcionCrearLicencias)
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

bAcerca = Button(raiz, text="Acerca de", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray", command=acercaDe)
bAcerca.configure(cursor="hand2")
bAcerca.place(x=340, y=320)

bSalir = Button(raiz, text="Salir", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray",command=salirPrograma)
bSalir.configure(cursor="hand2")
bSalir.place(x=240, y=420)



