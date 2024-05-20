from queue import Queue
import time

# Створити чергу заявок
queue = Queue()

# Функція для генерації заявки та додавання її до черги
def generate_request():
    # Створити нову заявку (можна використовувати будь-які дані для ідентифікації)
    new_request = "New request"
    # Додати заявку до черги
    queue.put(new_request)
    print("New request generated and added to the queue.")

# Функція для обробки заявки з черги
def process_request():
    # Якщо черга не пуста:
    if not queue.empty():
        # Видалити заявку з черги
        request = queue.get()
        # Обробити заявку (можна додати обробку заявки)
        print("Processing request:", request)
    else:
        # Якщо черга порожня, вивести повідомлення
        print("The queue is empty. No requests to process.")

# Головний цикл програми з обробкою KeyboardInterrupt для виходу з програми
try:
    while True:
        # Виконати генерацію заявок
        generate_request()
        # Виконати обробку заявок
        process_request()
        # Затримка перед наступною ітерацією (імітація реального часу обробки)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nProgram interrupted by the user. Exiting...")