class NumberListProcessor:
    def __init__(self, input_list):
        #Конструктор класса. Оставляет только числовые элементы (int и float).
        self.numbers = [x for x in input_list if isinstance(x, (int, float))]
    
    def display_list(self):
        #Выводит содержимое числового списка.
        print("Содержимое списка:", self.numbers)
    
    def calculate_average(self):
        #Вычисляет среднее значение элементов списка.
        if not self.numbers:
            return 0  # Возвращаем 0, если список пуст
        return sum(self.numbers) / len(self.numbers)


# Пример использования
if __name__ == "__main__":
    # Создаем объект с разными типами данных
    test_list = [10, "hello", 3.14, None, 42, "world", 7.5]
    processor = NumberListProcessor(test_list)
    
    # Выводим отфильтрованный список
    processor.display_list()  
    
    # Вычисляем и выводим среднее значение
    average = processor.calculate_average()
    print(f"Среднее значение: {average:.2f}")  