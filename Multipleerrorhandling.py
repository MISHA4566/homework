def process_user_input(user_input):
    try:
        # Розділення рядка на числа за допомогою коми та перетворення на список цілих чисел
        numbers = [int(num) for num in user_input.split(',')]
        return numbers
    except ValueError:
        print("Помилка: введено неправильне значення. Будь ласка, введіть числа, розділені комами.")
        return []
    except IndexError:
        print("Помилка: доступ до індексу, що виходить за межі діапазону.")
        return []

# Отримання рядка від користувача
user_input = input("Введіть список чисел, розділених комами: ")

# Обробка введеного рядка та отримання списку чисел
numbers_list = process_user_input(user_input)

# Виведення результату
if numbers_list:
    print("Список цілих чисел:", numbers_list)