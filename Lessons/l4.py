import time
def func0(arg):
    arg.append(1)

our_list = [1,2,3,4,5]

func0(our_list)
print(our_list)


def func(arg1):
    arg1 += "asdasda"

our_string = "123"

func(our_string)
print(our_string)


def greet(*args, **kwargs):
    print(args)
    print(kwargs)

greet (1,2,3,4,56,"asds", name = "Maksim", age = 19, sex = "male")

def func1(x,y=2):
    return x**y

print(func1(3,5))

def func2(z = None):
    if z is None:
        z = []
    z.append(1)
    print(z)
func2()

def func3(data, *, start = 1,end = 5):
    print(data,start,end)
func3(1)

def func4(x,y):
    print(x,y)

def func5(data, f):
    f(*data)
func5([3,4], func4)

def func6(x):
    def func7(y):
        print(x*y)
    return func7
f=func6(5)
f(4)

def timer(f):
    def wraper(*args, **kwargs):
            current_time = time.time()
            result = f(*args, **kwargs)
            print(time.time() - current_time)
            return result
    return wraper


def long_fanc():
    time.sleep(1)

long_fanc = timer(long_fanc)
long_fanc()