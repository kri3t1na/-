# Создаем класс Interpreter
class Interpreter:
    # Создаем экземпляр класса
    def __init__(self):
        self.operator = {'and': '&', 'or': '|', 'not': '~'}

    # Функция interpreter заменяет операторы
    def interpreter(self, replace_str):
        for i, j in self.operator.items():
            replace_str = replace_str.replace(i, j)
        return replace_str


def main():
    # Определяем переменную interp как класс Interpreter
    interp = Interpreter()
    # Открываем файл для чтения
    with open('test.py', 'r') as prog:
        # Читаем файл
        bool_op = prog.read()
    # Обращаемся к функции interpreter для замены операторов
    bin_op = interp.interpreter(bool_op)
    # Открываем файл для записи
    with open('test.py', 'w') as prog:
        # Записываем изменения в файл
        prog.write(bin_op)
        # Закрываем файл
        prog.close()


main()
