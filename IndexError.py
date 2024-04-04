try:
    my_list = [1, 2, 3]
    index = 5
    value = my_list[index]
    print("Значення за індексом", index, ":", value)
except IndexError:
    print("Помилка: неправильний індекс")
