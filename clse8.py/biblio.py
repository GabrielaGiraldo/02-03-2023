class Persona():
    
    def __init__(self):
        self.ID = int(input("Ingrese su ID:"))
        self.nombre = input("Ingrese su nombre:")  
        self.info = {
            "ID":self.ID,
            "Nombre":self.nombre,
            "Libros":
                {
                    "ID":self.ID,
                    "Info":{}
                    
                    }
            
        }
    def __str__(self) -> str:
        cantidad_libros = len(self.info["Libros"])
        return f"{self.ID}:{self.nombre} = tiene {cantidad_libros} prestados"
    def agregar_libro(self):
        libro = input("Ingrese el nombre de su libro:")
        fecha = str(input("Ingrese la fecha en la que fue prestado:"))
        libro_prestado = {
            "Nombre":libro,
            "Fecha":fecha,
            "Estado":"Prestado"
        }
        self.info["Libros"].update(libro_prestado)
    
    def visualizar_libros(self):
         print(self.info)
    def devolver_libro(self):
        libro = str(input("Libro a regresar:"))
        for i in self.info["Libros"]:
            if i["Nombre"] == libro:
                print("Si está")
                i["Estado"] = "Devuelto"
    def eliminar(self):
        x = input("¿Desea eliminar un libro? (si/no):")
        x = x.lower()
        if x == "si":
            lib = input("¿Qué libro desea eliminar?")
            lib = lib.lower()
            self.info["Libro"].pop(lib)
            print(self.info)
pers = Persona()
pers.agregar_libro()
print("\n")
pers.devolver_libro()
print("\n")
pers.visualizar_libros()
print("\n")
pers.eliminar()
print(pers)
    # while True:
    #     print(
    #         """_
    #         1.Ingresar usuario
    #         2.Cantidad de libros prestados
    #         3.Agregar libro
    #         4.Devolver libro
    #         5.Visualizar usuario
    #         6.Eliminar libro
    #         (x). Salir
        
    #     """)
    #     pers = Persona(input("¿Qué desea hacer?"))
    #     match pers:
            
    #         case "1":
    #             print(agregar_user())
    #         case "2":
    #             print()
    #         case "3":
    #             print()
    #         case "4":
    #             print()
    #         case "5":
    #             print()
    #         case "6":
    #             print()
    #         case "x":
    #             print("Salio de la biblioteca")
    #             break