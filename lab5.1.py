# Создаем класс бинарного дерева поиска
class BiTree:
    # Функция, создающая экземпляр класса (узел дерева)
    def __init__(self, key='*'):
        self.left = '*'
        self.right = '*'
        self.key = key

    # Функция, представляющая экземпляр класса в виде строки
    def __str__(self):
        return "[%s, %s, %s]" % (self.left, self.key, self.right)
    

    # Функция создания нового узла
    def isEmpty(self):
        return self.left == self.right == self.key == '*'

    # Функция вставки нового узла в бинарное дерево поиска
    def insert(self, key):
        if self.isEmpty():
            self.key = key
        # Проверяем является ли значение узла равным значению корня дерева
        elif key == self.key:
            self.key = key
        # Если введенный ключ меньше имеющегося переходим к левому поддереву
        elif key < self.key:
            # Проверка на наличие узлов слева
            if self.left == '*':
                self.left = BiTree(key)
            # Обращаемся к функции вставки для рассмотрения поддерева
            else:
                self.left.insert(key)
        # Если введенный ключ больше имеющегося переходим к правому поддереву
        else:
            # Проверка на наличие узлов справа
            if self.right == '*':
                self.right = BiTree(key)
            # Обращаемся к функции вставки для рассмотрения поддерева
            else:
                self.right.insert(key)


# Ввод количества узлов в бинарном дереве поиска
print("Введите количество узлов бинарного дерева поиска")
N = int(input())
# Ввод корня дерева
print("Введите корень дерева")
root = BiTree(int(input()))
# Ввод значений узлов
for i in range(N):
    print("Введите значение узла(ключ)")
    root.insert(int(input()))
    # Вывод построенного дерева
    print("Бинарное дерево поиска", root)


