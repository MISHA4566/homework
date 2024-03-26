def copy_file(source_file, destination_file):
    try:
        # Відкриття файлів для читання та запису
        with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
            # Копіювання вмісту з одного файлу в інший
            content = source.read()
            destination.write(content)
        print(f"Файл '{source_file}' успішно скопійовано у файл '{destination_file}'.")
    except FileNotFoundError:
        print("Помилка: один з файлів не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

# Виклик функції для копіювання файлу
copy_file('example.txt', 'example1.txt')