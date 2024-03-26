def write_to_file(user_input, filename):
    try:
        with open(filename, 'w') as file:
            file.write(user_input)
        print(f"Рядок '{user_input}' успішно записано у файл '{filename}'.")
    except Exception as e:
        print(f"Помилка при записі у файл: {e}")

user_text = input("Введіть рядок для запису у файл: ")
write_to_file(user_text, 'example.txt')