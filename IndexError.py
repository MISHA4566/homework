def write_to_file(user_input, filename):
    try:
        # Відкриття файлу для запису
        with open(filename, 'w') as file:
            # Запис рядка у файл
            file.write(user_input)
        print(f"Рядок '{user_input}' успішно записано у файл '{filename}'.")
    except IndexError:
        print("Помилка: неправильний індекс у списку.")
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")

# Отримання рядка від користувача
user_text = input("Введіть рядок для запису у файл: ")

# Виклик функції для запису у файл
write_to_file(user_text, 'feli.txt')