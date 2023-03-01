class SerVivo():
    sentidos_listo = ["Olfato","Vista","Tacto","Gusto","Oido"]
    
    def __init__(self,nombre):
        self.nombre = nombre
    
    def sentido(self):
        print(self.sentidos_listo)
    
    def movimiento(self):
        print(f"{self.nombre} se esta moviendo")
    
    def sonido(self):
        print(f"{self.nombre} esta haciendo un sonido")

class Persona(SerVivo):
    
    def movimiento(self):
        print(f"{self.nombre} esta bailando en la calle")
    
    def sonido(self):
        print(f"{self.nombre} esta cantando TQG")


class Gato(SerVivo):
    
    def movimiento(self):
        print(f"{self.nombre} esta peleandose con otro")
    
    def sonido(self):
        print(f"{self.nombre} esta ronroneando")

class Perro(SerVivo):
    
    def movimiento(self):
        print(f"{self.nombre} esta cruzando la calle")
    
    def sonido(self):
        print(f"{self.nombre} esta gañiando")

p1 = Persona("Gabriela")
p1.movimiento()
p1.sonido()
p1.sentido()
print("\n")
g = Gato("Cheshire")
g.movimiento()
g.sonido()
g.sentido()
print("\n")
pr = Perro("Estrella")
pr.movimiento()
pr.sonido()
pr.sentido()