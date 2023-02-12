def ver(
    diccionario:dict
) -> dict:
     x = str(input("Desea ver un usuario? (si/no) "))
     x = x.lower()
     if x == "si":
         z = str(input("Que usuario desea visualizar:"))
         diccionario.items(z)

     else:
         print("No se desea ver ningun usuario")
print("-"*40)