class Robot():
    x = 0
    y = 0
    def __init__(self,nom):
        self.nom = nom
    def arriba(self):
        g = int(input("Cuantos espacios quiere subir:"))
        self.y = self.y + g
    def abajo(self):
        g = int(input("Cuantos espacios quiere bajar:"))
        self.y = self.y - g
    def izquierda(self):
        g = int(input("Cuantos espacios quiere moverse a la izquierda:"))
        self.x = self.x - g
    def derecha(self):
        g = int(input("Cuantos espacios quiere moverse a la derecha:"))
        self.x = self.x + g
    def posicion(self):
        print(f"Esta en la posición ({self.x},{self.y})")

bot = Robot("Karolai")
bot.arriba()
bot.abajo()
bot.izquierda()
bot.derecha()
bot.posicion()
print(bot)
    
        