#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 04/06/2023 12:25am
#Ultima version: 04/06/2023 1:30pm
#Version: 3.10.6

import bs4
import requests
import archivos
import names
import random
from clases import Licencia
import datetime

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
    archivos.guardarTexto("test", ".xml", tagTipo)
    return tipoLicencias
   
def crearLicencias(pLista, pCantidad):
    for i in range(pCantidad):
        nuevaLicencia = Licencia()
        nuevaLicencia.asignarCedula(crearCedula(pLista))
        nuevaLicencia.asignarNombre(f"{names.get_first_name()} {names.get_last_name()} {names.get_last_name()}")
        nuevaLicencia.asignarNacimiento(f"{random.randint(1,28)}-{random.randint(1,12)}-{random.randint(1900,2023-19)}")
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



if __name__ == "__main__":
    conseguirTipoLicencias()