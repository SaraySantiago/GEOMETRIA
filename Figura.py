#C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

class figura: 
    
    __dimensiones = []
    __color = None
    
    def __init__(self, dimensions=[1,1], color = None) -> None:
          self.__dimensiones  = dimensions 
          
    def getDimensiones(self):
     return self.__dimensiones 
    
    def perimetro(self):
        return 5

    def area(self):
        return 5
    
    def __str__(self) -> str:
        answ = f"figura: area: {self.area()} perimetro: {self.perimetro()}" 
        return answ

if __name__ == "__main__":
    
    f0 = figura() 
    print (f0)
    f1 = figura([2]) 
    print (f1)
    f3 = figura([2,3]) 
    print (f3)