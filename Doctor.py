class Doctor:

 #CONSTRUCTOR
    def __init__(self,nombre,apellido,nacimiento,sexo,username,contra,especialidad,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.sexo = sexo
        self.username = username
        self.contra = contra
        self.especialidad= especialidad
        self.telefono = telefono


 #METODO GET
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getNacimiento(self):
        return self.nacimiento

    def getSexo(self):
        return self.sexo

    def getUsername(self):
        return self.username

    def getContra(self):
        return self.contra

    def getEspecialidad(self):
        return self.especialidad    

    def getTelefono(self):
        return self.telefono    


          #METODO SET
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setNacimiento(self, nacimiento):
        self.nacimiento = nacimiento

    def setSexo(self, sexo):
        self.sexo = sexo
    
    def setUsername(self, username):
        self.username = username
    
    def setContra(self, contra):
        self.contra = contra
    
    def setEspecialidad(self, especialidad):
        self.especialidad = especialidad

    def setTelefono(self, telefono):
        self.telefono = telefono