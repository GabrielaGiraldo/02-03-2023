class Triangulo():
    
    def __init__(self,nombre):
        self.nombre = nombre
        self.a = int(input("Introduce el lado a"))
        self.b = int(input("Introduce el lado b"))
        self.c = int(input("Introduce el lado c"))
        self.lados = [self.a,self.b,self.c]
    
    def lado_mayor(self):
        may = max(self.lados)
        print(may)
    
    def tipo_tria(self):
        conjunto_lados = set(self.lados)
        if len(conjunto_lados) == 3:
            print(f"{self.nombre} es un triángulo escaleno")
        elif len(conjunto_lados) == 2:
            print(f"{self.nombre} es un triángulo isoseles")
        elif len(conjunto_lados) == 1:
            print(f"{self.nombre} es un triángulo equilatero")
            
#set es para cambiar las cosas a conjuntos, en los conjuntos los datos no se repiten
tri = Triangulo("Triangulito")
tri.lado_mayor()

