from l7 import Alarm

class My_BD:

    def init_mongo():
        pass
    
    def init_postrgesql():
        pass

    @classmethod
    def get(cls, bd_type):
        if bd_type == "mongo":
            result = cls()
            result.init_mongo()
        else:
            result = cls()
            result.init_postrgesql()


class My_BD1:

    field = 10

    @classmethod
    def chto_to(cls):
        cls.field = 20

print(My_BD1.field)
My_BD1.chto_to()
print(My_BD1.field)


            
class My_BD3:

    def __init__(self):
        self.one = 1 #public
        self._two = 2 #protected
        self.__three = 3 #private

    def onem(self):
        pass

    def _twom(self):
        self.__threem()
    
    def __threem(self):
        print(self.__three)
        print(self.__three)
        print(self.__three)
a = My_BD3()
print(a.one)
print(a._two)
#print(a.__three)

a.onem()
a._twom()
#a.__threem()



# a = 1
# b = 2

# c = Alarm()
# d = Alarm()

# print(a+b)
# print(c+d)

class Vector:
    x = 0
    y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

       
    def __add__(self,other):
        self.x += other.x
        self.y += other.y
        
    def __str__(self):
        return f"x={self.x} y={self.y}"
    
    def __enter__(self):
        print("enter")
    
    def __exit__(self, exception_type, exception_value, traceback):
        print("exit")
a = Vector(1,2)
b = Vector(5,8)
print(Vector.y, Vector.x)
a+b
print(a.x,a.y)
print(a)

with Vector(1,2) as Vector:
    pass

class Clock:
    current_seconds = 0
    current_minutes = 0
    current_hours = 0

    alarm_time = (3,30,0)
    alarm_is_set = True
    
    def __init__(self,h=0,m=0,s=0):
        self.set_time(h,m,s)
        

    def set_time(self,h,m,s):
        assert h < 24, "h<24"
        assert m < 60, "h<60"
        assert s < 60, "h<60"
        self.current_hours = h
        self.current_minutes = m
        self.current_seconds = s

    @staticmethod
    def _to_double_numbers(self, x):
        if (x < 10):
            return f"0{x}"
        else:
            return x

    def show_time(self):
        h = self._to_double_numbers(self.current_hours)
        m = self._to_double_numbers(self.current_minutes)
        s = self._to_double_numbers(self.current_seconds)
        print(f"{h}:{m}:{s}")




    
class Alarm(Clock):
    def __init__(self, h, m, s):
        super().__init__(h, m, s)
        self.y = 10



a = Alarm(0,0,0)
print(a.y)
print(a.show_time)