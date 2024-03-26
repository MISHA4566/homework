def compare_files(file1, file2):
    # Відкриття файлів для читання
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        # Читання вмісту файлів у список рядків
        lines_file1 = f1.readlines()
        lines_file2 = f2.readlines()

        # Порівняння рядків і виведення відсутніх у другому файлі
        for line in lines_file1:
            if line not in lines_file2:
                print(line.strip())

# Виклик функції для порівняння файлів
compare_files('example.txt', 'example1.txt')