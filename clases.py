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

    def asignarCedula(self,pCedula):
        """
        Funcionalidad: Asigna la cedula
        Entrada: el número de cedula (string)
        Salida: Asigna un numero al atributo cedula del paciente
        """   
        self.cedula=pCedula
        return
    
    def asignarNombre(self,pNombre):
        """
        Funcionalidad: Asigna el nombre
        Entrada: el nombre del paciente (string)
        Salida: Asigna un nombre al atributo nombreCompleto del paciente
        """   
        self.nombreCompleto=pNombre
        return
    
    def asignarNacimiento(self,pNacimiento):
        """
        Funcionalidad: Asigna el correo
        Entrada: el correo electronico (string)
        Salida: Asigna un str al atributo correo del paciente
        """   
        self.nacimiento=pNacimiento
        return
    
    def asignarExpedicion(self,pExpedicion):
        """
        Funcionalidad: Asigna la cedula
        Entrada: el número de cedula (string)
        Salida: Asigna un numero al atributo cedula del paciente
        """   
        self.expedicion=pExpedicion
        return
    
    def asignarVencimiento(self,pVencimiento):
        """
        Funcionalidad: Asigna el estado de activo
        Entrada: el estado de activo (bool)
        Salida: Asigna un estado al atributo activo del paciente
        """   
        self.vencimiento=pVencimiento
        return
    

    def asignarLicencia(self,pLicencia):
        """
        Funcionalidad: Asigna la cedula
        Entrada: el número de cedula (string)
        Salida: Asigna un numero al atributo cedula del paciente
        """   
        self.tipoLicencia=pLicencia
        return
    
    def asignarSangre(self,pSangre):
        """
        Funcionalidad: Asigna el nombre
        Entrada: el nombre del paciente (string)
        Salida: Asigna un nombre al atributo nombreCompleto del paciente
        """   
        self.tipoSangre=pSangre
        return
    
    def asignarDonador(self,pDonador):
        """
        Funcionalidad: Asigna el correo
        Entrada: el correo electronico (string)
        Salida: Asigna un str al atributo correo del paciente
        """   
        self.esDonador=pDonador
        return
    
    def asignarSede(self,pSede):
        """
        Funcionalidad: Asigna la cedula
        Entrada: el número de cedula (string)
        Salida: Asigna un numero al atributo cedula del paciente
        """   
        self.sede=pSede
        return
    
    def asignarPuntaje(self,pPuntaje):
        """
        Funcionalidad: Asigna el estado de activo
        Entrada: el estado de activo (bool)
        Salida: Asigna un estado al atributo activo del paciente
        """   
        self.puntaje=pPuntaje
        return
    
    def asignarCorreo(self,pCorreo):
        """
        Funcionalidad: Asigna el estado de activo
        Entrada: el estado de activo (bool)
        Salida: Asigna un estado al atributo activo del paciente
        """   
        self.correo=pCorreo
        return


    def mostrarCedula(self):
        """
        Funcionalidad: Devuelve el numero de cedula
        Entrada: N/A
        Salida: Número de cedula del paciente
        """   
        return self.cedula
    
    def mostrarNombre(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.nombreCompleto

    def mostrarNacimiento(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.nacimiento
    
    def mostrarExpedicion(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.expedicion
    
    def mostrarVencimiento(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.vencimiento
    
    def mostrarLicencia(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.tipoLicencia
    
    def mostrarSangre(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.tipoSangre
    
    def mostrarDonador(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.esDonador
    
    def mostrarSede(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.sede
    
    def mostrarPuntaje(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.puntaje
    
    def mostrarCorreo(self):
        """
        Funcionalidad: Devuelve el nombre
        Entrada: N/A
        Salida: Nombre del paciente
        """   
        return self.correo
    
    def indicarDatos(self):
        return self.cedula, self.nombreCompleto, self.nacimiento, self.expedicion, self.vencimiento, self.tipoLicencia, self.tipoSangre, self.esDonador, self.sede, self.puntaje, self.correo
