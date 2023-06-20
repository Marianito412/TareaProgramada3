#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 04/06/2023 12:25am
#Ultima version: 04/06/2023 1:30pm
#Version: 3.10.6

import bs4
import requests
import archivos
import names
import random
import datetime
from clases import Licencia
import datetime
import pdfkit
import os
#import pandas as pd

x = datetime.datetime.now()

def crearCedula(pPadron):
    """
    Funcionalidad: Crea una cédula única
    Entradas:
    -pPadron: El padron para verificar que la cédula sea única
    Salidas:
    -cedula: La cédula generada
    """
    cedulas = [persona.mostrarCedula() for persona in pPadron]
    while True:
        cedula = f"{random.randint(1,9)}-{random.randint(0, 9999):04}-{random.randint(0, 9999):04}"
        if cedula not in cedulas:
            return cedula

def crearTag(pEtiqueta, pContenido, pAtributo=""):
    """
    Funcionalidad: Crea un string con formato html/xml válido
    Entradas:
    -pEtiqueta(str): El nombre de la etiqueta
    -pContenido(str): El contenido de esa etiqueta
    -pAtributo(str): Cualquier atributo deseado
    """
    pContenido = pContenido.replace("\n", "\n\t")
    return f"<{pEtiqueta} {pAtributo}>\n\t{pContenido}\n</{pEtiqueta}>"

def conseguirTipoLicencias():
    url = "https://practicatest.cr/blog/licencias/tipos-licencia-conducir-costa-rica"
    pagina = requests.get(url).content
    pagina = bs4.BeautifulSoup(pagina, "html.parser")
    texto = pagina.find(class_ = "content-blog")
    tagTipo = ""
    tipoLicencias = []
    for tipo in texto.find_all("h2"):
        subtipos = ""
        for subtipo in texto.find_all("h3"):
            if subtipo.findPreviousSibling("h2") == tipo:
                tipoLicencias.append(subtipo.text.strip())
                tagSubtipo = ""
                info = subtipo.findNextSiblings()[:4]
                tagSubtipo += crearTag("nombre", subtipo.text.strip())
                tagSubtipo += crearTag("comentario", info[0].text.strip())
                tagSubtipo += crearTag("requisitos", info[3].text)
                tagSubtipo = crearTag("subtipo", tagSubtipo)
                subtipos += tagSubtipo
        tagTipo += crearTag("tipo", subtipos, pAtributo=f"nombre='{tipo.text.strip()}'")
    archivos.guardarTexto("TiposDeLicencias", ".xml", tagTipo)
    return tipoLicencias

def generarHTML(persona: Licencia):
    plantilla = archivos.cargarTexto("plantilla", ".html")
    plantilla = plantilla.format(
        cedula=f"CI-{persona.mostrarCedula()[0]}{persona.mostrarCedula()[2:6]}{persona.mostrarCedula()[7:]}",
        expedicion=persona.mostrarExpedicion(),
        nacimiento=persona.mostrarNacimiento(),
        vencimiento=persona.mostrarVencimiento(),
        tipo=persona.mostrarLicencia(),
        EsDonador="Donador" if persona.mostrarDonador() else "No Donador",
        sangre=persona.mostrarSangre(),
        nombre = persona.mostrarNombre(),
        creacion = datetime.datetime.now().strftime("%d-%m-%Y %H:%M" ),
        sede = persona.mostrarSede()
    )
    archivos.guardarTexto("generado", ".html", plantilla, encoding="utf-8")

def generarPDF(pLicencias, pCedula):
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    for persona in pLicencias:
        persona : Licencia = persona
        print(persona.mostrarCedula(), pCedula)
        print(persona.mostrarCedula() == pCedula)
        if persona.mostrarCedula() == pCedula:
            print(persona.mostrarCorreo())
            generarHTML(persona)
            pdfkit.from_file("generado.html", "Licencia.pdf", css="style.css", configuration=config)
            return True
    #generarHTML(pLicencias[0])
    #pdfkit.from_file("generado.html", "test.pdf", configuration=config, options={"user-style-sheet": "style.css"})
    #print()
    print(pCedula)
    return False

def filtrarLista(pLista, pFiltros=[]):
    for licencia in pLista:
        if all([filtro(licencia) for filtro in pFiltros]):
            yield licencia

def generarFila(pAtributos):
    separador = ", "
    return separador.join([str(i) for i in pAtributos])

def generarReporte(pLista: list, pEncabezados: list, pExtraerDatos, pFiltros):
    archivo = generarFila(pEncabezados) + "\n"
    for licencia in filtrarLista(pLista, pFiltros):
        archivo += generarFila(pExtraerDatos(licencia)) + "\n"
    return archivo

def conseguirEdad(persona: Licencia):
    return int(persona.mostrarNacimiento().split("-")[-1])

def generarCorreo(persona: Licencia):
    nombres = persona.mostrarNombre().split(" ")
    return f"{nombres[1]}{nombres[2][0]}{nombres[0][0]}@gmail.com"

def determinarSede(pPersona: Licencia):
    provincia = int(pPersona.mostrarCedula()[0])
    sedesPorProvincia = {
        1:["Dirección General de Educación Vial", ""],
        8:["Dirección General de Educación Vial", ""],
        9:["Dirección General de Educación Vial", ""],
        2:["Dirección General de Educación Vial", ""],
        3:["Dirección General de Educación Vial licencias Cartago"],
        4:["Dirección General de Educación Vial licencias Heredia"],
        5:["Dirección General de Educación Vial licencias Liberia",
           "Dirección General de Educación Vial licencias Nicoya"],
        6:["Dirección General de Educación Vial licencias Puntarenas",
           "Dirección General de Educación Vial licencias Rio Claro"],
        7:["Dirección General de Educación Vial licencias Guapiles",
           "Dirección General de Educación Vial licencias Lim+ón"]
    }
    return random.choice(sedesPorProvincia[provincia])

def crearLicencias(pLista, pCantidad):
    tipoLicencias = conseguirTipoLicencias()
    for i in range(pCantidad):
        nuevaLicencia = Licencia()
        nuevaLicencia.asignarCedula(crearCedula(pLista))
        nuevaLicencia.asignarNombre(f"{names.get_first_name()} {names.get_last_name()} {names.get_last_name()}")
        nuevaLicencia.asignarNacimiento(f"{random.randint(1,28)}-{random.randint(1,12)}-{random.randint(1900,2023-19)}")
        nuevaLicencia.asignarExpedicion(datetime.date.today().strftime("%d-%m-%Y"))
        nuevaLicencia.asignarVencimiento((datetime.date.today() + datetime.timedelta(days= 365*3 if conseguirEdad(nuevaLicencia)<25 else 365*5)).strftime("%d-%m-%Y"))
        nuevaLicencia.asignarLicencia(random.choice(tipoLicencias))
        nuevaLicencia.asignarSangre(random.choice(["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB"]))
        nuevaLicencia.asignarDonador(bool(random.randint(0,1)))
        nuevaLicencia.asignarSede(determinarSede(nuevaLicencia))
        nuevaLicencia.asignarPuntaje(random.randint(0,12))
        nuevaLicencia.asignarCorreo(generarCorreo(nuevaLicencia))
        pLista.append(nuevaLicencia)
    for persona in pLista:
        print(persona.indicarDatos())
    print (pLista)
    return pLista

def renovarLicencias(licencias, pCedula):
    for persona in licencias:
        if persona.mostrarCedula() == pCedula:
            persona.asignarExpedicion(x.strftime("%d-%m-%Y"))
            nacimiento=(persona.mostrarNacimiento().split('-'))[2]
            edad= int(x.strftime("%Y")) - int(nacimiento) 
            if edad > 25:
                annio= str(int(x.strftime("%Y")) + 5)
            else:
                annio= str(int(x.strftime("%Y")) + 3)
            persona.asignarVencimiento(x.strftime("%d-%m")+"-"+annio)
            print(persona.indicarDatos())
    print(licencias)
    return licencias

def reporteTipoLicencia(pLicencias, tipoLicencia):
    
    def extraerDatosTipoLicencia(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarLicencia()]

    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "Tipo de licencia"], extraerDatosTipoLicencia, [lambda x: x.mostrarLicencia()==tipoLicencia])
    archivos.guardarTexto(f"Reporte{tipoLicencia}", ".csv", reporte, encoding="utf-8")

def reporteSancion(pLicencias):

    def extraerDatosSancion(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarLicencia(), pPersona.mostrarPuntaje()]

    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "Tipo de licencia", "Puntaje"], extraerDatosSancion, [lambda x: x.mostrarPuntaje()<=6 and x.mostrarPuntaje()>0])
    archivos.guardarTexto("ReporteSanción", ".csv", reporte, encoding="utf-8")

def reporteTotal(pLicencias):

    def extraerDatosTotal(pPersona: Licencia):
        return pPersona.indicarDatos()

    reporte = generarReporte(pLicencias, ['Cédula', 'Nombre', 'FechaNac', 'FechaExp', 'FechaVenc', 'TipoLicen', 'TipoSangre', 'Donador', 'Sede', 'Puntaje'], extraerDatosTotal, [])
    archivos.guardarTexto("ReporteTotal", ".csv", reporte, encoding="utf-8")

def reporteDonador(pLicencias):

    def extraerDatosDonantes(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarLicencia()]

    def filtrarDonante(pPersona: Licencia):
        if pPersona.mostrarDonador():
            return True
        else:
            return False

    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "Tipo de licencia"], extraerDatosDonantes, [filtrarDonante])
    archivos.guardarTexto("ReporteDonante", ".csv", reporte)

def reporteDonador2(licencias):
    cedulas=[]
    nombres=[]
    tipos=[]
    for persona in licencias:
        if persona.mostrarDonador():
            cedulas.append(persona.mostrarCedula())
            nombres.append(persona.mostrarNombre())
            tipos.append(persona.mostrarLicencia())
            
    file_path = 'C:/Users/Usuario/Documents/GitHub/TareaProgramada3.xlsx'
    writer = pd.ExcelWriter(file_path)
    df = pd.DataFrame({'Cedula': cedulas,
                    'Nombre': nombres,
                    'TipoLicen': tipos})
    #df = df[['Id', 'Nombre', 'Apellido']]
    #writer = ExcelWriter('C:/Users/Usuario/Documents/GitHub/TareaProgramada3.xlsx')
    df.to_excel(writer, 'Hoja de datos', index=False)
    writer.close()

    return licencias

if __name__ == "__main__":
    #os.system(f"wkhtmltopdf generado.html 'C:/Users/Usuario/Desktop/a.pdf'")
    lista = crearLicencias([], 10)
    generarPDF(lista, "a")
    #print(generarReporte(lista, ["Nombre", "Sangre"], lambda x: [x.mostrarNombre(), x.mostrarSangre()], []))
    