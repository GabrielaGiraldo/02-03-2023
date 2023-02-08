import math
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
print("\n")

def distancia_dos_puntos(
        x_1:float,
        x_2:float,
        y_1:float,
        y_2:float
            
) -> float:
    """
    Función que calcula la distancia de dos puntos
    
    ---parametros---
    - (x = math.pow(x_2 - x_1,2)): es la resta de (x2-x1) elevado a la 2
    - (y = math.pow(y_2 - y_1,2)): es la resta de (y2-y1) elevado a la 2
    - (d = math.sqrt(x+y)) : es para aplicar la raiz los productos de (x) y (y)
    ---return(d)---
    
    """
    x = math.pow(x_2 - x_1,2)
    y = math.pow(y_2 - y_1,2)
    d = math.sqrt(x+y)
    return(d)   
x_1 = float(input("Ingrese el valor 1 de x:"))
x_2 = float(input("Ingrese el valor 1 de x:"))
y_1 = float(input("Ingrese el valor 1 de x:"))
y_2 = float(input("Ingrese el valor 1 de x:"))
result= distancia_dos_puntos(x_1,x_2,y_1,y_2)
print(result)