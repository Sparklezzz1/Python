import my_modules.MyLib1
from my_modules.MyLib import f as fx3
from my_modules.MyLib1 import f as fx5
from my_modules import *
try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter another number: "))
    answer = userInput1/userInput2
    print ("The answer is ", answer)
    assert True, 'ALARM'#Если написать False программа выдаст ошибку
except ValueError:
    print ("Error: You did not enter a number")
except ZeroDivisionError:
    print ("Error: Cannot divide by zero")
except Exception as e:
    print ("Unknown error: ", e)
else:
    print("else")
finally:
    print("finally")


print(fx3(3))
print(fx5(3))
print(dir(my_modules.MyLib1))#Показывает что мы можем сделать с чем-угодно в питоне