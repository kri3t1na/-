import sys


# Создаем класс стек
class Stack:
    # Инициализируем новый пустой стек
    def __init__(self):
        self.items = []

    # Проверяем пуст ли стек
    def empty(self):
        return self.items == []

    # Фукнция добавления нового элемента в конец стека
    def push(self, item):
        self.items.append(item)

    # Функция удаления последнего элемента стека
    def pop(self):
        return self.items.pop()

    # Функция, определяющая размер стека
    def size(self):
        return len(self.items)

    # Функция вывода всего содержания стека
    def full(self):
        return self.items

    # Функция очистки стека
    def clear(self):
        return self.items.clear()

    # Функция вывода последнего элемента стека, не удаляя его
    def back(self):
        return self.items[-1]


# Определяем переменную а как стек
a = Stack()

# Выводим список возможных команд
print("Command list:")
print("push - adding an element to the back")
print("pop - deleting an element to the back")
print("back - output of the last element")
print("size - output stack size")
print("empty - check for presence of elements")
print("clear - clearing of the stack")
print("exit - exit the program")
print("Enter a command:")
# Запускаем цикл выбора команд для стека
while True:
    # Ввод команды
    c = input()

    # Добавляем элемент в конец стека
    if c == "push":
        # Ставим условие, чтобы количество элементов стека было меньше 100
        if a.size() == 100:
            # Выводим сообщение о том, что стек заполнен
            print("The stack is full.")
        a.push(input())
        print("The contents of the stack:", a.full())

    # Удаляем последний элемент стека
    if c == "pop":
        # Проверка стека, пуст ли он
        if a.empty():
            print("Error")
        else:
            a.pop()
            print("The contents of the stack:", a.full())


    # Вывод последнего элемента стека
    if c == "back":
        if a.empty():
            print("Error")
        else:
            a.back()
            print("Last stack item '", a.back(), "'")

    # Определяем размер стека
    if c == "size":
        print("Size the stack", a.size())

    # Проверка стека пуст ли он
    if c == "empty":
        print("The stack is empty:", a.empty())

    # Очищаем стек
    if c == "clear":
        a.clear()
        print("The contents of the stack:", a.full())

    # Завершаем программу
    if c == "exit":
        print("Bye")
        sys.exit()
