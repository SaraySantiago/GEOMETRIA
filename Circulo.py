#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

from Figura import figura

class circulo(figura): # Los circulos SON figuras. Tiene ya lo mismo que figura. 
    
    def __init__(self, dimensions=...) -> None:
        super().__init__(dimensions)


if __name__ == "__main__": 
    
    c0 = circulo()
    print(c0)

    
    