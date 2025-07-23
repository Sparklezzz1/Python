import re
text = input("Введите строку \n")
longest_word = ""
litterss = {}

for litters in text:
      if litters.isalpha():
            litters = litters.lower()
            litterss[litters] = litterss.get(litters,0)+1
result_litters = litterss

words = text.lower().split()
unique_words = set(words)
count_unique_words = len(unique_words)

for word in words:
        longest_word = re.sub(r'[^а-яА-ЯёЁ\s]', ' ', word)
        if len(word) > len(longest_word):
            longest_word = word

print(f"Количество уникальных слов: {count_unique_words}") 
print(f"Самое длинное слово: {longest_word}")
print(f"Частота букв: {result_litters}")

