class SerVivo():
    def __init__(self,nom,x=0,y=0):
        self.nom = nom
        self.x = x
        self.y = y
    def horizontal(self):
        n = int(input(f"Cuantos espacios quiere que se mueva {self.nom} horizontalmente:"))
        self.x = self.x + n
    def vertical(self):
        n = int(input(f"Cuantos espacios quiere que se mueva {self.nom} verticalmente:"))
        self.y = self.y + n
    def posicion(self):
        print(f"{self.nom} esta en la posición ({self.x},{self.y})")
        
class Persona(SerVivo):
    def horizontal(self):
        n = int(input(f"Cuantos espacios quiere que se mueva {self.nom} horizontalmente:"))
        self.x = (self.x + (n+4))
    def vertical(self):
        n = int(input(f"Cuantos espacios quiere que se mueva {self.nom} verticalmente:"))
        self.y = (self.y + (n+4))
    def posicion(self):
        print(f"{self.nom} esta en la posición ({self.x},{self.y})")

class Gato(SerVivo):
    def horizontal(self):
        n = int(input(f"Cuantos espacios quiere que se mueva {self.nom} horizontalmente:"))
        self.x = (self.x + (n+3))
    def vertical(self):
        n = int(input(f"Cuantos espacios quiere que se mueva {self.nom} verticalmente:"))
        self.y = (self.y + (n+3))
    def posicion(self):
        print(f"{self.nom} esta en la posición ({self.x},{self.y})")

class Perro(SerVivo):
    def horizontal(self):
        n = int(input(f"Cuantos espacios quiere que se mueva {self.nom} horizontalmente:"))
        self.x = (self.x + (n+2))
    def vertical(self):
        n = int(input(f"Cuantos espacios quiere que se mueva {self.nom} verticalmente:"))
        self.y = (self.y + (n+2))
        
    def posicion(self):
        print(f"{self.nom} esta en la posición ({self.x},{self.y})")

p1 = Persona("Gabriela")
p1.horizontal()
p1.vertical()
p1.posicion()
print("\n")
g = Gato("Cheshire")
g.horizontal()
g.vertical()
g.posicion()
print("\n")
pr = Perro("Estrella")
pr.horizontal()
pr.vertical()
pr.posicion()
