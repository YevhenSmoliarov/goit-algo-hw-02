def are_brackets_balanced(input_string):
    stack = []
    # Словник для відображення відкриваючих і закриваючих дужок
    brackets_map = {"(": ")", "[": "]", "{": "}"}
    # Перебираємо символи у введеному рядку
    for char in input_string:
        # Якщо символ - відкриваюча дужка, додаємо її в стек
        if char in brackets_map.keys():
            stack.append(char)
        # Якщо символ - закриваюча дужка
        elif char in brackets_map.values():
            # Якщо стек порожній або остання відкриваюча дужка не відповідає поточній закриваючій дужці,
            # то дужки несиметричні
            if not stack or brackets_map[stack.pop()] != char:
                return "Несиметрично"
    # Якщо стек не порожній після перевірки усіх символів, то дужки несиметричні
    if stack:
        return "Несиметрично"
    # Якщо всі дужки були збалансовані, повертаємо "Симетрично"
    return "Симетрично"

# Приклад використання:
input_strings = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for input_string in input_strings:
    print(f"{input_string}: {are_brackets_balanced(input_string)}")