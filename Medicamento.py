class Medicamento:
  
  #CONSTRUCTOR
    def __init__(self,nombre,precio,descripcion,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad

       

    #METODO GET
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio
    
    def getDescripcion(self):
        return self.descripcion
    
    def getCantidad(self):
        return self.cantidad

   #METODO SET
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPrecio(self, precio):
        self.precio = precio
    
    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setCantidad(self, cantidad):
        self.cantidad = cantidad