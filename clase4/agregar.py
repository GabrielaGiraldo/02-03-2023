from datetime import date

def agregar_usuario(
    diccionario:dict
)-> dict:
    x = input("¿Desea agregar un nuevo usuario? (si/no):")
    y = x.lower()
    if y == "si":
        
        nom = input("Ingrese su nombre: ")
        n = nom.lower()
        lib =  input("Ingrese su libro: ")
        estado = input("Estado:")
        fecha_pres =  input(f"l fecha de prestamo es {date.today()}")
    
        diccionario_int = {
            "libro":lib,
            "fecha":fecha_pres,
            "estado": estado
        }
    else: 
        print("No desea añadir ningun usuario")
    if diccionario.get(n) != None:
        diccionario[n].append(diccionario_int)
    else:
        diccionario[n] = [diccionario_int]
    print(diccionario)