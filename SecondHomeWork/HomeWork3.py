import re
data = [
    "  Иван Иванов  ", 
    "Петров;Петр ", 
    "Сидорова Анна ", 
    "  ОЛЕГ КУЗНЕЦОВ  ", 
    "МАРИЯ; ТРОФИМОВА"
]
normalized = []
for i in data:
    cleaned = re.sub(r'[^а-яА-ЯёЁ\s]', ' ', i)
    cleaned = cleaned.strip()
    cleaned = cleaned.lower()
    cleaned = cleaned.title()
    cleaned = cleaned.split()
    if len(cleaned) == 2:
        first, second = cleaned
        if len(first) > len(second):
            cleaned = [second, first]
    normalized.append(" ".join(cleaned)) 
print(normalized)
