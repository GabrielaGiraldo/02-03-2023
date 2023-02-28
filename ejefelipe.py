class Robot():
    #x = 0
    #y = 0
    def __init__(self,nom,x,y):
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

bot = Robot("Karolai",0,0)
bot.horizontal()
bot.vertical()
print(bot)