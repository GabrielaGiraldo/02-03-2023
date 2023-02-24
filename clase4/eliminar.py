def eliminar_usuario(
    diccionario:dict
)-> dict:
    x = input("¿Desea eliminar un usuario? (si/no):")
    y = x.lower()
    if y == "si":
        nom = input("Que usuario desea eliminar: ")
        n = nom.lower()
        del diccionario[n]
    else: 
        print("No desea eliminar ningun usuario")
    print(diccionario)