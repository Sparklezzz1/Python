a = 123
print(type(a))
if isinstance(a, int):
    print("Это число")
elif type(a) is str:
    print("Это строка")
else:
    print("Не знаю что это")

a=123
b=123
print (a==b)
print (a is b)
a=[1,2,3]
b=a.copy()
a.append(4)
print(a,b)

c=[
    "Валера",
    "Олег",
    "Сергей",
    "Иван"
]

for student in c:
    print (student, end=" ")
    print(len(student), end=" ")
    if len(student) >= 5:
        print("Отчислен")
    else:
        print("Принят")
    
    
print("Программа завершена1")


d=[
    "Валера",
    "Олег",
    "Сергей",
    "Иван"
]

for student in d:
    if len(student) <= 5:
       print(student, "Принят", len(student))
    break
    
    
print("Программа завершена2")

e=[
    "Валера",
    "Олег",
    "Сергей",
    "Иван",
    "Дмитрий"
]

for student in e:
    if len(student) >= 5:
       continue
    print(student, "Принят", len(student))

    
    
print("Программа завершена3")\



for i in range(1,11):

    if i%2 == 0:
        if i == 10:
            print(i)
        else:
            print(i, end=", ")




q = 0

while q < 30:
    q += 1
    l=q
    q=40
    q=l
    print(q)
            