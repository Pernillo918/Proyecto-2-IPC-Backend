class Cita:
  
  #CONSTRUCTOR
    def __init__(self,fecha,hora,motivo,paciente,estado,doctor):
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.paciente = paciente
        self.estado = estado
        self.doctor = doctor

       

    #METODO GET
    def getFecha(self):
        return self.fecha
    
    def getHora(self):
        return self.hora
    
    def getMotivo(self):
        return self.motivo
    
    def getPaciente(self):
        return self.paciente

    def getEstado(self):
        return self.estado

    def getDoctor(self):
        return self.doctor

   #METODO SET
    def setFecha(self, fecha):
        self.fecha = fecha
    
    def setHora(self, hora):
        self.hora = hora
    
    def setMotivo(self, motivo):
        self.motivo = motivo

    def setPaciente(self, paciente):
        self.paciente = paciente

    def setEstado(self, estado):
        self.estado = estado

    def setDoctor(self, doctor):
        self.doctor = doctor