#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

from Figura import figura

class circulo(figura): # Los circulos SON figuras. Tiene ya lo mismo que figura. 
    
# TODO elevar color a la superclase
    
    def __init__(self, dimensions=...) -> None:
        super().__init__(dimensions)


if __name__ == "__main__": 
    
    f0 = figura() 
    print (f0.getDimensiones())
    c0 = circulo()
    print(c0.getDimensiones())


    
