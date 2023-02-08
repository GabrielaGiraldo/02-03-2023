def area_rectangulo(
        x:float,
        y:float
) -> float:
    """
    Función que calcula el area de un rectangulo
    
    ---parametros---
    - x (float): es la base de mi rectangulo
    - y (float): es la altura de mi rectangulo
    
    ---return---
    - area(float): es el area del rectangulo
    """
    area = x*y
    return area
area= float(input("Introduce el lado del rectangulo:"))
base= float(input("Introduce la base del rectangulo:"))
result = area_rectangulo(area,base)
print(result)