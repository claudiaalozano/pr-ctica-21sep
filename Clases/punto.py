
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