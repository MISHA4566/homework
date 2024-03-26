try:
    # Отримання двох інпутів від користувача
    input1 = input("Введіть перше число: ")
    input2 = input("Введіть друге число: ")

    # Конвертація інпутів до чисел
    number1 = float(input1)
    number2 = float(input2)

    # Виведення результату
    print("Перше число:", number1)
    print("Друге число:", number2)

except ValueError:
    print("Помилка: введено нечислове значення.")
