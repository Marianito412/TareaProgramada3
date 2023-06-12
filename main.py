#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 04/06/2023 12:25am
#Ultima version: 04/06/2023 1:30pm
#Version: 3.10.6

from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

bXML = Button(raiz, text="Crear XML", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
bXML.configure(cursor="hand2")
bXML.place(x=130, y=120)

bLicencias = Button(raiz, text="Crear licencias", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
bLicencias.configure(cursor="hand2")
bLicencias.place(x=340, y=120)

bRenovar = Button(raiz, text="Renovar licencias", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
bRenovar.configure(cursor="hand2")
bRenovar.place(x=130, y=220)

bPDF = Button(raiz, text="Generar PDF", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
bPDF.configure(cursor="hand2")
bPDF.place(x=340, y=220)

bExcel = Button(raiz, text="Reportes de Excel", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
bExcel.configure(cursor="hand2")
bExcel.place(x=130, y=320)

bAcerca = Button(raiz, text="Acerca de", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
bAcerca.configure(cursor="hand2")
bAcerca.place(x=340, y=320)

bSalir = Button(raiz, text="Salir", width=20, height=3, font=("Arial", 10), activebackground="#fbd404",bg="lightgray")
bSalir.configure(cursor="hand2")
bSalir.place(x=240, y=420)



