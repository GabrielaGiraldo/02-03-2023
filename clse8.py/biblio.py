class Persona():
    
    def __init__(self,ID,nombre):
        self.ID = ID
        self.nombre = nombre
        self.info = {
            "ID":self.ID,
            "Nombre":self.nombre,
            "Libros":
                {
                    "ID":ID,
                    "Info":{}
                    
                    }
            
        }
    def __str__(self) -> str:
        cantidad_libros = len(self.info["Libros"])
        return f"{self.ID}:{self.nombre} = tiene {cantidad_libros} prestados"
    def agregar_libro(self,libro,fecha):
        libro_prestado = {
            "Nombre":libro,
            "Fecha":fecha,
            "Estado":"Prestado"
        }
        self.info["Libros"].append(libro_prestado)
    
    def visualizar_libros(self):
        print(self.info["Libros"])
    def devolver_libro(self,libro):
        for i in self.info["Libros"]:
            if i["Nombre"] == libro:
                print("Si está")
                i["Estado"] = "Devuelto"

pers = Persona("1","Kaizer")
pers.agregar_libro()
print(pers)
pers.visualizar_libros()