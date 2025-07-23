template = [1,"a",2,"b",3,"c",4,"d",5] 
new_list=[]
new_list = [el for el in template if isinstance(el, str)]
print(new_list)

a = [1,2,3,4,5,6,7,8,9,10]
b = {"a":1, "b":2, "c":3}
c = "abcdefghikjlmnop"
print(len(a))
print(1 in a)
print(len(b))
print("a" in b)
print(1 in b.values())
print(b.values())
print(("b",3) in b.items())
print(len(c))
print("z" in c )
print("d1" in c)
for x,y in b.items():
    #print(x)
    print(x,y)
   # print(b[x])
print(min(a))
print(max(a))
print(sum(a))
print(min(b))
print(max(b))
print(min(c))
print(max(c))
print(a.count(2))
print(c.count("d"))
print(a.index(2))
print(c.index("d"))
d = a.copy()
print(d)
b.clear()
print(b)
my_tuple=('a','b','a')
my_list = list(my_tuple)
my_set = set(my_tuple)
my_frozenset = frozenset(my_tuple)
print(my_tuple,my_list,my_set,my_frozenset)
my_dict = {'z':10,"a":4,"p":8}
print(my_dict)
a1 = [1,2,3]
b1 = tuple(a1)
#b1[1] = 3
print(b1)
print(c[-1])
print(a[-1])
s="Hello, world!!!"
print(s[:5])
print(s[7:12])
print(s[7:12:2])
print(s[7:-1])
print(s[:-1])
n=c[:len(c)//2]
print(n)
n=c[::-1]
print(n)
n=c[5:0:-1]
print(n)
n=c[0:5:1]
print(n)
a[1:7] = [10]
print(a)
a = [(1,2,3),(4,[1,2,3,4],6),(7,8,9),10]
a[1:2] = "x"
print(a)
a = [(1,2,3),(4,[1,2,3,4],6),(7,8,9),10]
b = a[1]
print(b)
c = b[1]
print(c)
d = c[2]
print(d)
a = [(1,2,3),(4,[1,2,3,4],6),(7,8,9),10]
b = a[1][1][2]
print(b)
a = [123,43,-67,35,2321,9]
b = sorted(a)
print(b)
print(a)
a.sort()
print(a)
a = [123,43,-67,35,2321,9]
b = reversed(a)
print(b)
print(a)
a.reverse()
print(a)
a,b = [1,2,3],[4,5]
print([a,b])
print([*a,*b])
b=5
a.insert(0,b)
print(a)
dict1={'a':1, 'b':2}
dict2={'c':3, 'd':4}
dict1["e"] = 10
print(dict1)
print(dict1|dict2)
dict1.update(dict2)
print(dict1)
print({x for x in range(10)})
a = {"a":1,"b":2}
b = {"a":3,"c":4}
print({**a,**b})
a = r'asdasfasf \t sa'
print(a)
print(len(a))
print(a[-1])
print("asdsaf"+"sdafsafas")
print("sadfa" * 3)
b = "asdasfasfsaf"
c = '''asdsafsafa'''
d = """
    asfagasgas
    fsafsafsaf
    fasfsafasfsa
    """
print(d)
student = {
    "name": "Вася",
    "age": 20,
}
hello = "Привет, я - " + student["name"]  + " и мне " +  str(student["age"])  + " лет"
print(hello) 
hello = f"Привет, я - {student['name']} и мне {student['age']} лет"
print(hello) 
hello = "Привет, я - {name} и мне {age} лет".format(**student)
print(hello)
a = ["Вася", 20]
hello = "Привет, я - {0} и мне {1} лет".format(*a)
print(hello)
s="asdasdsad"
print(s.encode())