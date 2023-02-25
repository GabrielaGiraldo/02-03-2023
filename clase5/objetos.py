class personas():
    libros = {}
    def __init__(self,nombre):
        self.nombre = nombre
    def agregar(self,nom_libro,fecha):
        self.libros.update({nom_libro:fecha})

p1 = personas("felipe")
p2 = personas("gabriela")
print(p1.libros)
p1.agregar("python","24/02/2023")
p1.agregar("java","25/02/2023")

p2.agregar("python","24/02/2023")
p2.agregar("java","25/02/2023")
print(p1.libros)
print(p2.libros)