class Employee:
    def __init__(self, name, _salary):
        self.name = name
        self._salary = _salary
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
    
    @property
    def salary(self):
        return self._salary
    
    def set_salary(self, value):
        if value < 0:
            raise ValueError("Дайте деняг!!! :C")
        object.__setattr__(self, '_salary', value)  
   
    def __setattr__(self, name, value):
        if name == "_salary" and hasattr(self, "_salary"):
            raise AttributeError("Нельзя менять salary напрямую! Используйте set_salary().")
        super().__setattr__(name, value)
        

class Manager(Employee):
    def __init__(self, name, _salary, departament):
        super().__init__(name, _salary)
        self.departament = departament

    def display_info(self):
        super().display_info()
        print(f"Departament: {self.departament}")
      
class Developer(Employee):
    def __init__(self, name, _salary, programming_language):
        super().__init__(name, _salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"ProgrammingLanguage: {self.programming_language}")
   

dev = Developer("Alice", 5000, "Python")
dev.display_info()
dev.set_salary(1000123)
dev.display_info()
dev.set_salary(-1000)
