class MyClass:
    def __init__(self, input_list):
       
        self.numbers = [x for x in input_list if isinstance(x, (int, float))]
    
    def display_list(self):
       
        print("Содержимое списка:", self.numbers)
    
    def calculate_average(self):
   
        if not self.numbers:
            return 0  
        return sum(self.numbers) / len(self.numbers)



test_list = [0, "hello", 23.4, None, 42, "world", 123.5]
    
processor = MyClass(test_list)
   
processor.display_list()  
    
average = processor.calculate_average()
print(f"Среднее значение: {average:.2f}")  