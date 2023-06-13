#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 04/06/2023 12:25am
#Ultima version: 04/06/2023 1:30pm
#Version: 3.10.6

import bs4
import requests
from clases import tipoLicencia

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
    Licencias = texto.find_all("h3")[1:]
    tipos = []
    for articulo in Licencias:
        articulo.find
        tipo = articulo.findPreviousSibling("h2")
        subtipo = articulo.text.strip()
        info = articulo.findNextSiblings()[:4]
        comentario = info[0]
        requisitos = info[3]
        tipos.append(tipoLicencia(tipo, subtipo, comentario, requisitos))
        print(tipos[-1])
        


if __name__ == "__main__":
    conseguirTipoLicencias()