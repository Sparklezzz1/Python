litters_lower = "аеёиоуыэюя"
litters_upper = "АЕЁИОУЫЭЮЯ"
result = []
text = input("Введите текст \n ")
for i in text:
    if i in litters_lower:
        index = litters_lower.index(i)
        result.append(litters_lower[index + 1])
    elif i in litters_upper:
        index = litters_upper.index(i)
        result.append(litters_upper[index + 1])
    else:
        result.append(i)
result_str = "".join(result)
print("Зашифровонная строка:")
print(result_str)