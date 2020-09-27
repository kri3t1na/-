import sys


# Создаем класс дек
class Deque:
    # Инициализируем новый пустой дек
    def __init__(self):
        self.items = []

    # Проверяем пуст ли дек
    def is_empty(self):
        return self.items == []

    # Фукнция добавления нового элемента в конец дек
    def push_back(self, item):
        self.items.append(item)

    # Фукнция добавления нового элемента в начало дека
    def push_front(self, item):
        self.items.insert(0, item)

    # Функция удаления последнего элемента дека
    def pop_back(self):
        return self.items.pop()

    # Функция удаления первого элемента дека
    def pop_front(self):
        return self.items.pop(0)

    # Функция, определяющая размер дека
    def size(self):
        return len(self.items)

    # Функция вывода всего содержания дека
    def full(self):
        return self.items

    # Функция очистки дека
    def clear(self):
        return self.items.clear()

    # Функция вывода последнего элемента дека, не удаляя его
    def back(self):
        return self.items[-1]

    # Функция вывода первого элемента дека, не удаляя его
    def front(self):
        return self.items[0]


# Определяем переменную а как дек
a = Deque()

# Выводим список возможных команд
print("List of commands:")
print("push_back - adding an element to the back")
print("push_front - deleting an element from the front")
print("pop_back - adding an element to the back")
print("pop_front - deleting an element from the front")
print("front - output of the first element")
print("back - output of the last element")
print("size - output deque size")
print("empty - check for presence of elements")
print("clear - clearing of the deque")
print("exit - exit the program")
print("Enter a command:")
# Запускаем цикл выбора команд для дека
while True:
    # Ввод команды
    c = input()
    # Ставим условие, чтобы количество элементов дека было меньше 100
    if a.size() == 100:
        # Выводим сообщение о том, что дек заполнен
        print("The deque is full.")

    # Добавляем элемент в конец дека
    if c == "push_b":
        a.push_back(input())
        print("The contents of the deque:", a.full())

    # Удаляем последний элемент дека
    if c == "pop_b":
        # Проверка дека, пуст ли он
        if a.is_empty():
            print("Error")
        else:
            a.pop_back()
            print("The contents of the deque:", a.full())

    # Добавляем элемент в начало дека
    if c == "push_f":
        a.push_front(input())
        print("The contents of the deque:", a.full())

    # Удаляем элемент с конца дека
    if c == "pop_f":
        # Проверяем пуст ли дек
        if a.is_empty():
            print("Error")
        else:
            a.pop_front()
            print("The contents of the deque:", a.full())

    # Вывод первого элемента дека
    if c == "front":
        if a.is_empty():
            print("Error")
        else:
            a.front()
            print("First deque item '", a.front(), "'")

    # Вывод последнего элемента дека
    if c == "back":
        if a.is_empty():
            print("Error")
        else:
            a.back()
            print("Last deque item '", a.back(), "'")

    # Определяем размер дека
    if c == "size":
        print("Size the deque", a.size())

    # Проверка дека пуст ли он
    if c == "empty":
        print("The deque is empty:", a.is_empty())

    # Очищаем дек
    if c == "clear":
        a.clear()
        print("The contents of the deque:", a.full())

    # Завершаем программу
    if c == "exit":
        print("Bye")
        sys.exit()
