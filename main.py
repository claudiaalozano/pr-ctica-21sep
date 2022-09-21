if __name__ == "__main__":
    
    
    seleccon = input("Selecciona Punto o Rectangulo: ")
    if seleccon == "Punto":
        from Clases.punto import *
        print(Punto())
    if seleccon == "Rectangulo":
        from Clases.rectangulo import *
        print(Rectangulo())