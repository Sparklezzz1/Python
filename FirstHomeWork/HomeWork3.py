students = [
    ("Иван", "Петров", [4, 5, 5, 4], [3, 4, 5, 3], 0.9),
    ("Мария", "Иванова", [5, 5, 5, 5], [5, 5, 4, 5], 0.95),
    ("Алексей", "Сидоров", [3, 4, 3, 3], [4, 3, 4, 4], 0.7),
    ("Елена", "Козлова", [5, 4, 5, 5], [4, 5, 5, 5], 0.85),
    ("Дмитрий", "Смирнов", [2, 3, 2, 3], [3, 2, 2, 3], 0.5)
]
for student in students:    
    if student[4] < 0.75:
        print("Прогульщики:", student)
    else:
        continue


print()

for student in students:
    avg_mark = (sum(student[2])/len(student[2])+sum(student[3])/len(student[3]))/2
    #avg_mark=round(avg_mark)
    if avg_mark > 4.75:
        print("Почти отличница:", student)
    else:
        continue
   

print()


for student in students:
    avg_mark_python = sum(student[2])/len(student[2])       
    avg_mark_math = sum(student[3])/len(student[3])
    if avg_mark_python < avg_mark_math:
        print(student[0],student[1],"НУЖНО УДЕЛИТЬ БОЛЬШЕ ВНИМАНИЯ PYTHON!!!!!!!!")
    else:
        continue


