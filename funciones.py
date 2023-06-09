#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 04/06/2023 12:25am
#Ultima version: 19/06/2023 1:30pm
#Version: 3.10.6

#Importación de bibliotecas
import bs4
import requests
import archivos
import names
import random
import datetime
from clases import Licencia
import datetime
import pdfkit

x = datetime.datetime.now()

#Definición de funciones
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
    """
    Funcionalidad: Conseguir los tipos de licencias y cargarlos a un archivo XML
    Entradas: NA
    Salidas: tipoLicencias (list): La lista de los tipos de licencias
    """
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
    """
    Funcionalidad: Genera el HTML sobre el cual generar el PDF
    Entradas: persona (Licencia): La licencia para generar el html
    Salidas: NA
    """
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
    """
    Funcionalidad: Generar el pdf con la información de la persona
    Entradas:
    -pLicencias(list): La lista de licencias
    -pCedula(str): La cédula de la licencia a generar
    Salidas: NA
    """
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
    print(pCedula)
    return False

def filtrarLista(pLista, pFiltros=[]):
    """
    Funcionalidad: Filtra una lista dada basado en funciones filtro
    Entradas:
    -pLista(list): La lista a filtrar
    -pFiltros(list): La lista de filtros 
    Salidas:
    -licencia(Licencia): La licencia que cumple con los requisitos
    """
    for licencia in pLista:
        if all([filtro(licencia) for filtro in pFiltros]):
            yield licencia

def generarFila(pAtributos):
    """
    Funcionalidad: Genera una fila de un csv
    Entradas: -pAtributos(list): La lista de atributos
    Salidas:
    return(str): El texto de la fila
    """
    separador = ", "
    return separador.join([str(i) for i in pAtributos])

def generarReporte(pLista: list, pEncabezados: list, pExtraerDatos, pFiltros):
    """
    Funcionalidad: Genera un reporte csv
    Entradas:
    -pLista(list): La lista de personas
    -pEncabezados(list): La lista de encabezados del reporte
    -pExtraerDatos(func): La función que extrae los datos necesarios
    -pFiltros(list): La lista de filtros a usar
    Salidas:
    .archivo(str): String con el reporte csv
    """
    archivo = generarFila(pEncabezados) + "\n"
    for licencia in filtrarLista(pLista, pFiltros):
        archivo += generarFila(pExtraerDatos(licencia)) + "\n"
    return archivo

def conseguirEdad(persona: Licencia):
    """
    Funcionalidad: La edad de la persona
    Entradas:
    -persona(Licencia): La persona
    Salidas:
    return(int): La edad de la persona
    """
    return int(persona.mostrarNacimiento().split("-")[-1])-2023

def generarCorreo(persona: Licencia):
    """
    Funcionalidad: Genera un correo basado en el nombre
    Entradas:
    -persona(Licencia): La persona a generar
    Salidas:
    -return(str): El correo generado
    """
    nombres = persona.mostrarNombre().split(" ")
    return f"{nombres[1]}{nombres[2][0]}{nombres[0][0]}@gmail.com"

def determinarSede(pPersona: Licencia):
    """
    Funcionalidad: Determina la sede donde se saca una licencia
    Entradas:
    -pPersona(Licencia): La Licencia 
    Salidas:
    -return(str): La sede determinada
    """
    provincia = int(pPersona.mostrarCedula()[0])
    sedesPorProvincia = {
        1:["Dirección General de Educación Vial licencias sede central",
           "Dirección General de Educación Vial licencias Heredia"],

        8:["Dirección General de Educación Vial licencias sede central",
            "Dirección General de Educación Vial licencias Heredia"],

        9:["Dirección General de Educación Vial licencias sede central",
           "Dirección General de Educación Vial licencias Heredia"],

        2:["Dirección General de Educación Vial licencias San Carlos",
            "Dirección General de Educación Vial licencias Alajuela",
            "Dirección General de Educación Vial licencias San Ramón"],

        3:["Dirección General de Educación Vial licencias Cartago"],

        4:["Dirección General de Educación Vial licencias Heredia"],

        5:["Dirección General de Educación Vial licencias Liberia",
           "Dirección General de Educación Vial licencias Nicoya"],

        6:["Dirección General de Educación Vial licencias Puntarenas",
           "Dirección General de Educación Vial licencias Rio Claro"],

        7:["Dirección General de Educación Vial licencias Guapiles",
           "Dirección General de Educación Vial licencias Limón"]
    }
    return random.choice(sedesPorProvincia[provincia])

def crearLicencias(pLista, pCantidad):
    """
    Funcionalidad: Crea una cantidad de licencias
    Entradas:
    -pLista: La lista de persona ya existentes
    -pCantidad(int): La cantidad de personas a generar
    Salidas:
    -pLista(List): La lista de personas modificada
    """
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
    """
    Funcionalidad: Renueva la licencia afectando la fecha de vencimiento
    Entradas:
    -licencias: Las licencias a buscar
    -pCedula: La cedula a encontrar
    Salidas:
    -licencias: Licencias actualizadas
    """
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
    return licencias

def reporteTipoLicencia(pLicencias, tipoLicencia):
    """
    Funcionalidad: Genera un reporte basado en el tipo de licencia
    Entradas:
    -pLicencias: Las licencias a usar en el reporte
    -tipoLicencia: El tipo de licencia
    Salidas: NA
    """
    def extraerDatosTipoLicencia(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarLicencia()]

    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "Tipo de licencia"], extraerDatosTipoLicencia, [lambda x: x.mostrarLicencia()==tipoLicencia])
    archivos.guardarTexto(f"Reporte{tipoLicencia}", ".csv", reporte)

def reporteSancion(pLicencias):
    """
    Funcionalidad: Genera un reporte de las persona con sanción
    Entradas:
    -pLicencias: Las licencias a usar
    Salidas: NA
    """
    def extraerDatosSancion(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarLicencia(), pPersona.mostrarPuntaje()]
    
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "Tipo de licencia", "Puntaje"], extraerDatosSancion, [lambda x: x.mostrarPuntaje()<=6 and x.mostrarPuntaje()>0])
    archivos.guardarTexto("ReporteSanción", ".csv", reporte)


def reporteTotal(pLicencias):
    """
    Funcionalidad: Genera un reporte de toda la BD
    Entradas:
    -pLicencias: Las licencias a usar
    Salidas: NA
    """
    def extraerDatosTotal(pPersona: Licencia):
        return pPersona.indicarDatos()

    reporte = generarReporte(pLicencias, ['Cédula', 'Nombre', 'FechaNac', 'FechaExp', 'FechaVenc', 'TipoLicen', 'TipoSangre', 'Donador', 'Sede', 'Puntaje'], extraerDatosTotal, [])
    archivos.guardarTexto("ReporteTotal", ".csv", reporte)

def reporteDonador(pLicencias):
    """
    Funcionalidad: Genera el reporte de donadores
    Entradas: pLicencias: Las licencias a generar
    """
    def extraerDatosDonantes(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarLicencia()]
    def filtrarDonante(pPersona: Licencia):
        if pPersona.mostrarDonador():
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "Tipo de licencia"], extraerDatosDonantes, [filtrarDonante])
    archivos.guardarTexto("ReporteDonante", ".csv", reporte)

def reporteAnulado(pLicencias):
    """
    Funcionalidad: Genera el reporte de personas con licencia anuladad
    Entradas: pLicencias: Las licencias a generar
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosAnulados(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede()]
    def filtrarAnulado(pPersona: Licencia):
        if pPersona.mostrarPuntaje()==0:
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede"], extraerDatosAnulados, [filtrarAnulado])
    archivos.guardarTexto("ReporteAnulado", ".csv", reporte)

def reporteSedeCentral(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
        
    def extraerDatosSedeCentral(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeCentral(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias sede central":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeCentral, [filtrarSedeCentral])
    archivos.guardarTexto("reporteSedeCentral", ".csv", reporte)

def reporteSedeAlajuela(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedeAlajuela(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeAlajuela(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias Alajuela":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeAlajuela, [filtrarSedeAlajuela])
    archivos.guardarTexto("reporteSedeAlajuela", ".csv", reporte)

def reporteSedeCartago(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedeCartago(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeCartago(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias Cartago":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeCartago, [filtrarSedeCartago])
    archivos.guardarTexto("reporteSedeCartago", ".csv", reporte)

def reporteSedeHeredia(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedeHeredia(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeHeredia(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias Heredia":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeHeredia, [filtrarSedeHeredia])
    archivos.guardarTexto("reporteSedeHeredia", ".csv", reporte)

def reporteSedeSanRamon(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedeSanRamon(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeSanRamon(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias San Ramón":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeSanRamon, [filtrarSedeSanRamon])
    archivos.guardarTexto("reporteSedeSanRamon", ".csv", reporte)

def reporteSedeGuapiles(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedeGuapiles(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeGuapiles(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias Guápiles":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeGuapiles, [filtrarSedeGuapiles])
    archivos.guardarTexto("reporteSedeGuapiles", ".csv", reporte)

def reporteSedeLimon(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedeLimon(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeLimon(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias Limón":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeLimon, [filtrarSedeLimon])
    archivos.guardarTexto("reporteSedeLimon", ".csv", reporte)

def reporteSedeLiberia(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedeLiberia(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeLiberia(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias Liberia":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeLiberia, [filtrarSedeLiberia])
    archivos.guardarTexto("reporteSedeLiberia", ".csv", reporte)

def reporteSedeNicoya(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedeNicoya(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeNicoya(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias Nicoya":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeNicoya, [filtrarSedeNicoya])
    archivos.guardarTexto("reporteSedeNicoya", ".csv", reporte)

def reporteSedePuntarenas(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedePuntarenas(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedePuntarenas(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias Puntarenas":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedePuntarenas, [filtrarSedePuntarenas])
    archivos.guardarTexto("reporteSedePuntarenas", ".csv", reporte)

def reporteSedePerezZeledon(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedePerezZeledon(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedePerezZeledon(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias Pérez Zeledón":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedePerezZeledon, [filtrarSedePerezZeledon])
    archivos.guardarTexto("reporteSedePerezZeledon", ".csv", reporte)

def reporteSedeGolfito(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedeGolfito(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeGolfito(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias Río Claro de Golfito":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeGolfito, [filtrarSedeGolfito])
    archivos.guardarTexto("reporteRioClaroDeGolfito", ".csv", reporte)

def reporteSedeSanCarlos(pLicencias):
    """
    Funcionalidad: Genera un reporte basado en una sede
    """
    def cambioDonador(pDato):
        if pDato== False:
            return "No es donador"
        else:
            return "Es donador"
    def extraerDatosSedeSanCarlos(pPersona: Licencia):
        return [pPersona.mostrarCedula(), pPersona.mostrarNombre(), pPersona.mostrarNacimiento(), pPersona.mostrarExpedicion(), pPersona.mostrarVencimiento(),pPersona.mostrarLicencia(), pPersona.mostrarSangre(), cambioDonador(pPersona.mostrarDonador()), pPersona.mostrarSede(), pPersona.mostrarPuntaje()]
    def filtrarSedeSanCarlos(pPersona: Licencia):
        if pPersona.mostrarSede()=="Dirección General de Educación Vial licencias San Carlos":
            return True
        else:
            return False
    reporte = generarReporte(pLicencias, ["Cédula", "Nombre", "FechaNac", "FechaExp", "FechaVenc", "TipoLicen", "TipoSangre", "Donador", "Sede","Puntaje"], extraerDatosSedeSanCarlos, [filtrarSedeSanCarlos])
    archivos.guardarTexto("reporteSedeSanCarlos", ".csv", reporte)

#Programa principal
if __name__ == "__main__":
    #os.system(f"wkhtmltopdf generado.html 'C:/Users/Usuario/Desktop/a.pdf'")
    lista = crearLicencias([], 10)
    generarPDF(lista, "a")
    #print(generarReporte(lista, ["Nombre", "Sangre"], lambda x: [x.mostrarNombre(), x.mostrarSangre()], []))
    