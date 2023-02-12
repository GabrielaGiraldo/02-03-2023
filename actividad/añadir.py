def añadir(
    diccionario:dict
) -> dict:
     x = str(input("Desea añadir un usuario? (si/no) "))
     x = x.lower()
     if x == "si":
         nom = str(input("Añadir usuario: "))
         nom = nom.lower()
         lib = str(input("Añadir libro del nuevo usuario: "))
         lib = lib.lower()
         diccionario.update({nom:lib})
     else:
         print("No se desea añadir ningun usuario")
print("-"*40)