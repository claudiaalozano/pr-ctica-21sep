# pr-ctica-21sep

Mi dirección de GitHub es: https://github.com/claudiaalozano/pr-ctica-21sep.git

Para elaborar esta práctica hemos elaborado dos clases, una llamada Punto donde nos muestra un punto por pantalla y en que eje se encuentra, y otra llamada rectágulo donde calcula la base, la altura y el área a partir de los puntos obtenidos con la clase punto. 

Código empleado en Punto: 
```
class Punto:

    def __init__(self, x, y, puntito , cuadrante):
        self.x()
        self.y()
        self.puntito()
        self.cuadrante()

    def x (self, x):
        self.x = int(input("Introduce el valor de la coordena X: "))
        if x == None:
            x = 0
    
    def y (self, y):
        self.y = int(input("Introduce el valor de la coordenada y: "))
        if y == None:
            y = 0
    
    def puntito (self, puntito):
        puntito = print("Las coorcenadas son (" , self.x,", " ,self.y , ")")

    def cuadrante(self, cuadrante, x, y):
        if x == 0:
            print("El punto se encuentra sobre el eje Y.")
        if y == 0:
            print("El punto se encuentra sobre el eje X.")
        else:
            print("El punto está sobre los dos ejes.")
   ```
  
  Código empleado en la clase Rectágulo:
  ```
  import math

class Rectangulo:

    def __init__(self, pbase, paltura, parea, base, area, altura):
        self.base = base
        self.altura = altura
        self.area = area

    def base (self, base, A, B):
        
        def A (self,A):
            from Clases.punto import puntito
            A = puntito()
        
        def B (self, B):
            from Clases.punto import puntito
            B = puntito()
        
        base = 

    def altura (self, altura):
        def C (self,C):
            from Clases.punto import puntito
            C = puntito()
        
        def D (self, D):
            from Clases.punto import puntito
            D = puntito()
        altura = 

    def area (self, area, base, altura):
        area = base * altura
```
