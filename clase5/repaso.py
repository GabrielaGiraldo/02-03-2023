diccionario  = {
    "nombre":"Gabriela"
    
}
diccionario["apellido"] = "Giraldo"
temp = {"edad":23,
        "sexo":"Femenino",
        "profesion":"estudiante"}

diccionario["Extra"] = temp
diccionario.update(temp)
#diccionario["Extra"].pop("sexo")
#diccionario["Extra"]["profesion"] = ["H","O","L","A"]
#print(diccionario["Extra"]["profesion"])
print(diccionario)
