def my_metaclass(name,parents,attributes):
    name = name + " meta "
    print(f"CREATING class {name}")
    def __add__(a,b):
        return a + b
    
    attributes["__add__"] = __add__
    
    return type(name,parents,attributes)

class A():
    pass
class B():
    pass
class C():
    pass
class D(A,B,C, metaclass = my_metaclass):
    pass

print(type(D),D.__name__)



    