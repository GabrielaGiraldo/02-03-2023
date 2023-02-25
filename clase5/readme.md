diccionario  = {
    "nombre":"Gabriela"
    
}
diccionario["apellido"] = "Giraldo"
temp = {"edad":23,
        "sexo":"Femenino",
        "profesion":"estudiante"}
#diccionario["Extra"] = temp(para aplicar que esta informacion, la contenida en temp, se vuelva el valor de una key)
#diccionario.update(temp) (concatena la informacion)
no se puede repetir la key de un diccionario, si eso pasa (en temp por ejemplo) se va a rescribir la   información
diccionario["Extra"] = temp
diccionario["Extra"].pop("sexo")
#diccionario["Extra"]["edad"] = "22" (Se usa para modificar la informacion que se encuentra dentro de un diccionario, dentro de otro diccionario)
diccionario["Extra"]["profesion"] = ["H","O","L","A"]
# ["H","O","L","A"] funciona como una lista, por ende se puede acceder a los metodos de una lista mediante este. En este caso se usa la lista para añadir varios "valores" a una clave del diccionario
diccionario["Extra"]["profesion"].append("Adios")
print(diccionario["Extra"]["profesion"])
print(diccionario)
# el update dentro de un diccionario debe ser mirado con cuidado, ya ue si se utilia la misma key, la informacion se va a sobrescribir. 
