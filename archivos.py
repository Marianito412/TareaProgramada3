#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 04/06/2023 12:25am
#Ultima version: 04/06/2023 1:30pm
#Version: 3.10.6

import pickle

def graba(nomArchGrabar, varGuardar):
    """
    Funcionalidad: Graba un archivo
    Entradas:
    -nomArchGrabar(str): Nombre del archivo a escribir
    -varGuardar(any): La variable a guardar
    Salidas: NA
    """
    try:
        f=open(nomArchGrabar,"wb")
        print("Grabando archivo: ", nomArchGrabar)
        pickle.dump(varGuardar,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee(nomArchLeer):
    #Función que lee un archivo con una lista de estudiantes
    """
    Funcionalidad: Lee un archivo
    Entradas:
    -nomArchGrabar(str): Nombre del archivo a leer
    Salidas: NA
    """
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        print("Leyendo archivo: ", nomArchLeer)
        lista = pickle.load(f)
        f.close()
    except FileNotFoundError:
        print("Archivo no encontrado: ", nomArchLeer)
    return lista

def guardarTexto(pNombre, pExtension, pContenido):
    """
    Funcionalidad: Guarda un archivo de texto
    Entradas:
    -pNombre(str): El nombre del archivo
    -pExtension(str): La extensión del archivo
    -pContenido(str): El texto a guardar en el archivo
    Salidas:NA
    """
    with open(f"{pNombre}{pExtension}", "w") as archivo:
        archivo.write(pContenido)