# n = input("Введите количество элементов последовательности: ")
# n = int(n)
# b = []
# for i in range(n):
#     a = input("Введите элемент: ")
#     a = int(a)
#     if isinstance(a,int):
#         b.append(a)
#     else:
#         print("Вы ввели неверный формат")

# print(min(b))
# print(max(b))



#TRY2

# b = []
# for i in range(10):
#         a = input("Введите элемент: ")
#         a = str(a)
#         if a.isdigit():
#             b.append(int(a))
#         else:
#             print("Вы ввели не верный формат данных, программа закончила работу")
#             break
# print("Минимальное значение равно:", min(b))
# print("Максимальное значение равно:", max(b))


#правильное решение 
# min = 9999999999999999
# max = -999999999999999
# while True:
#     value = input("Введите значение")
#     if value.isdigit():
#         value = int(value)
#     else:
#          break
#     if min > value:
#          min = value
#     if max < value:
#         max = value 
# print(f"min = {min}, max = {max}")




#правильно но короче
# min_value = 9999999999999999
# max_value = -999999999999999
# while True:
#     value = input("Введите значение")
#     try:
#         value = int(value)
#     except:
#         break
#     min_value = min(min_value, value)
#     max_value = max(max_value, value)
# print(f"min = {min_value}, max = {max_value}")


#правильно но еще короче, но не работает) 

# input_list = list(map(int, input("Введите последовательность чисел через запятую").split(", ")))
# min_value = min(input_list)
# max_value = max(input_list)
# print(min_value, max_value)

#правильно но еще короче, но не работает) 

input_list = input("Введите последовательность чисел через запятую").split(", ")
input_list2 = []
for value in input_list:
    try:
        input_list2.append(int(value))
    except:
        break   
min_value = min(input_list2)
max_value = max(input_list2)
print(min_value, max_value)