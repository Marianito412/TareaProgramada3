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

def conseguirEdad(persona: Licencia):
    return int(persona.mostrarNacimiento().split("/")[-1])

def generarCorreo(persona: Licencia):
    nombres = persona.mostrarNombre().split(" ")
    return f"{nombres[1]}{nombres[2][0]}{nombres[0][0]}@gmail.com"

def crearLicencias(pLista, pCantidad):
    tipoLicencias = conseguirTipoLicencias()
    for i in range(pCantidad):
        nuevaLicencia = Licencia()
        nuevaLicencia.asignarCedula(crearCedula(pLista))
        nuevaLicencia.asignarNombre(f"{names.get_first_name()} {names.get_last_name()} {names.get_last_name()}")
        nuevaLicencia.asignarNacimiento(f"{random.randint(1,28)}/{random.randint(1,12)}/{random.randint(1900,2023-19)}")
        nuevaLicencia.asignarExpedicion(datetime.date.today.strftime("%d/%m/%Y"))
        nuevaLicencia.asignarVencimiento(datetime.date.today.timedelta(years = "3" if conseguirEdad(nuevaLicencia)<25 else "5"))
        nuevaLicencia.asignarLicencia(random.choice(tipoLicencias))
        nuevaLicencia.asignarSangre(random.choice(["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB"]))
        nuevaLicencia.asignarDonador(bool(random.randint(0,1)))
        nuevaLicencia.asignarSede()
        nuevaLicencia.asignarPuntaje(random.randint(0,12))
        nuevaLicencia.asignarCorreo(generarCorreo(nuevaLicencia))
        pLista.append(nuevaLicencia)
    return pLista

if __name__ == "__main__":
    conseguirTipoLicencias()