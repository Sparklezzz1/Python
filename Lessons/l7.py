def gen():
    current = 2
    while current < 101:
        yield current
        current += 2

a = gen()
for x in a:
    print(x)

    

f = open('1.txt',"r")
print(f.read())
f.close()
f = open("1.txt","w")
f.write("Hello, world")
f.close()
with open('1.txt',"r") as f:
    print(f.read())

#----------------------------------------------
class Alarm:
    current_seconds = 0
    current_minutes = 0
    current_hours = 0

    alarm_time = (3,30,0)
    alarm_is_set = True
    
    def __init__(self,h,m,s):
        self.set_time(h,m,s)
        

    def set_time(self,h,m,s):
        assert h < 24, "h<24"
        assert m < 60, "h<60"
        assert s < 60, "h<60"
        self.current_hours = h
        self.current_minutes = m
        self.current_seconds = s

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

a = dict()
b = list()

alarm1 = Alarm(21,0,0)
alarm2 = Alarm(20,0,0)

alarm1.show_time()
alarm2.show_time()
