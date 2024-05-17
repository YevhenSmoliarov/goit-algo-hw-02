from collections import deque

def is_palindrome(input_string):
    # Перетворення вхідного рядка в нижній регістр та видалення пробілів
    input_string = input_string.lower().replace(" ", "")
    
    # Створення двосторонньої черги
    char_queue = deque()
    
    # Додавання символів рядка до черги
    for char in input_string:
        char_queue.append(char)
    
    # Порівняння символів з обох кінців черги, доки черга не стане порожньою або не залишиться один символ
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    # Якщо всі символи були співпадаючими, рядок є паліндромом
    return True

# Приклад використання:
input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))  # True