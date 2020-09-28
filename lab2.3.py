# Импортируем модуль heapq
import heapq

# Открываем файл с входными данными
f = open('new.txt', 'r')
# Читаем данный файл
data = f.read()
# Запускаем цикл работы
while True:
    # Выводим сообщение о выборе приоритетной очереди
    print("Select the priority queue option ('time', 'priority')\n"
          "exit the program with the 'exit' command")
    # Вводим команду
    a = input()
    # Определяем введенную команду
    if a == 'time':
        # Находим наименьшений элемент(наивысший приоритет)
        que = heapq.nsmallest(
         5, data.splitlines(), key=lambda x: int(x.split()[-1])
        )
        # Выводим приоритетную очередь
        print("Priority queue by time")
        print("\n".join(que))
    # Определяем введенную команду
    if a == 'priority':
        # Находим наименьшений элемент(наивысший приоритет)
        pri = heapq.nsmallest(
            5, data.splitlines(), key=lambda x: int(x.split()[0])
        )
        # Выводим приоритетную очередь
        print("Priority queue by position")
        print("\n".join(pri))
    # Определяем введенную команду
    if a == 'exit':
        # Завершаем программу
        print('Bye')
        exit()
