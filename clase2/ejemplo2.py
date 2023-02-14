lista_estudiante = ["David","Omar","Isaac"]
lista_profe = ["Felipe"]
def agregar(
    lista:list
    
    ) -> list:
    estudiante = input("Añadir:")
    lista.append(estudiante)
agregar(lista_estudiante)


def eliminar(
    lista:list
    
    ) -> list:
    estudiante = str(input("Ingresar persona a eliminar:"))
    lista.remove(estudiante)
eliminar(lista_estudiante)

def ver(
    lista:list
    ) -> list:
    x = str(input("Desea ver los usuarios (si/no):"))
    if x == "si":
        print(lista)
ver(lista_estudiante)
