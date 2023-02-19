import datetime
def agregar_usuario(
    diccionario:dict
)-> dict:
    x = input("Desea agregar un nuevo usuario (si/no):")
    y = x.lower()
    if y == "si":
        
        nom = input("Ingrese su nombre: ")
        nom = nom.lower()
        lib =  input("Ingrese su libro: ")
        estado = input("Estado:")
        fecha_pres =  input("Ingrese fecha de prestamo:")
        diccionario_int = {
            "libro":lib,
            "fecha":fecha_pres,
            "estado": estado
        }
    else: 
        print("No desea añadir ningun usuario")
    if diccionario.get(nom) != None:
        diccionario[nom].append(diccionario_int)
    else:
        diccionario[nom] = [diccionario_int]
    print(diccionario)
    
def eliminar_usuario(
    diccionario:dict
)-> dict:
    x = input("Desea eliminar un usuario (si/no):")
    y = x.lower()
    if y == "si":
        nom = input("Que usuario desea eliminar: ")
        nom = nom.lower()
        del diccionario[nom]
    else: 
        print("No desea eliminar ningun usuario")
    print(diccionario)

def visualizar_usuario(
    diccionario:dict
    )-> dict:
    x = input("Desea visulizar un usuario (si/no):")
    y = x.lower()
    if y == "si":
        for i in diccionario.items():
            acc = input("Desea visulizar un usuario en especifico (si/no):")
            if acc == "si":
                mostrar = input("Que usuario desea ver:")
                diccionario.get(mostrar)
            else:
                print(i)
                
    