#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 04/06/2023 12:25am
#Ultima version: 04/06/2023 1:30pm
#Version: 3.10.6

class Licencia:
    def  __init__(self):
        self.cedula = 0
        self.nombreCompleto = ""
        self.nacimiento = ""
        self.expedicion = ""
        self.vencimiento = ""
        self.tipoLicencia = ""
        self.tipoSangre = ""
        self.esDonador = False
        self.sede = ""
        self.puntaje = 0
        self.correo = ""
    #@Todo: Getters y setters


class tipoLicencia:
    def __init__(self, tipo, subtipo, comentarios, requisitos):
        self.tipo: str = tipo
        self.subtipo: str = subtipo
        self.comentarios: str = comentarios
        self.requisitos: list = requisitos
    
    def __str__(self) -> str:
        return (f"tipo: {self.tipo}\n"
                f"Subtipo: {self.subtipo}\n"
                f"Comentarios: {self.comentarios}\n"
                f"Requisitos: {self.requisitos}"
                )

    def getTipo(self):
        return self.tipo
    def getSubtipo(self):
        return self.subtipo
    def getComentarios(self):
        return self.comentarios
    def getRequisitos(self):
        return self.requisitos
    
    def setTipo(self, tipo):
        self.tipo = tipo
    def setSubtipo(self, subtipo):
        self.subtipo = subtipo
    def setTipo(self, comentarios):
        self.comentarios = comentarios
    def setTipo(self, requisitos):
        self.requisitos = requisitos
    