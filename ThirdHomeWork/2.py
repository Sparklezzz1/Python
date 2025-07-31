class MyClass:
    def __init__(self, *args):
        self.text_field = None
        self.number_field = None
        
        if len(args) != 2:
            return  
        
        arg1, arg2 = args
        
  
        if isinstance(arg1, str) and isinstance(arg2, str):
            self.text_field = arg1 + arg2
        
    
        elif isinstance(arg1, int) and isinstance(arg2, int):
            self.number_field = arg1 + arg2
        
        
        elif (isinstance(arg1, str) and isinstance(arg2, int)) or (isinstance(arg1, int) and isinstance(arg2, str)):
            if isinstance(arg1, str):
                self.text_field = arg1
                self.number_field = arg2
            else:
                self.text_field = arg2
                self.number_field = arg1

    def __str__(self):
        fields = []
        if self.text_field is not None:
            fields.append(f"text_field='{self.text_field}'")
        if self.number_field is not None:
            fields.append(f"number_field={self.number_field}")
        return f"MyClass({', '.join(fields)})"


my_object = MyClass("Hello", "World")
print(my_object)
my_object = MyClass(10, 20)
print(my_object)
my_object = MyClass("Age: ", 25)
print(my_object)  
my_object = MyClass(100, " dollars")  
print(my_object)      
