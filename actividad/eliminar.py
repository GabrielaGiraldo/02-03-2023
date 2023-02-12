
def eliminar(
    diccionario:dict
) -> dict:
     x = str(input("Desea eliminar un usuario? (si/no) "))
     x = x.lower()
     if x == "si":
         nom = str(input("Que usuario desea eliminar: "))
         nom = nom.lower()
         diccionario.pop(nom)
     else:
         print("No se desea eliminar ningun usuario")
print("-"*40)
        