def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print("Помилка: файл не знайдено.")
        return -1
    except Exception as e:
        print(f"Помилка: {e}")
        return -1


filename = input("Введіть назву текстового файлу: ")

word_count = count_words_in_file(filename)

if word_count != -1:
    print(f"Кількість слів у файлі '{filename}': {word_count}")
