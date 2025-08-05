class Temperature :

    def __init__(self,__celsius):
        self.__celsius = __celsius

    @property
    def celsius(self):
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < - 273.15:
            raise ValueError("Температура не проходит по условию!")
        self.__celsius = value
        
    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32
    

temp = Temperature(25)
print(temp.fahrenheit) 
temp.celsius = -300