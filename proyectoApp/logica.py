class Articulo:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        
    def __str__(self):
        return ("Titulo : ",self.titulo,
                "Descripcion : ", self.descripcion)


class Cliente:
    
    def __init__ (self, nombre, apellidos, telefono, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.telefono = telefono
        
    def __str__(self):
        return ("Nombre: ", self.nombre,
                "Apellidos: ", self.apellidos,
                "Teléfono: ", self.telefono)
                
        
 