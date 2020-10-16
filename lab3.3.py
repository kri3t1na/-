# Вводим размер будущей хеш-таблицы
print("Enter the hash table size:")
N = int(input())
size = N
# Задаем хеш-таблицу как список
h = []
# Счетчик заполняемости хеш-таблицы
count = 0
# Создаем хеш-таблицу
for i in range(N):
    sl = ['', '', '']
    h.append(sl)
print("Empty hash table", h)
# Запускаем цикл работы с хеш-таблицей
while True:
    # Вводим команду
    print('')
    print("Enter the command(add, find, delete, exit:)")
    command = str(input())
    # Команда добавления ключа
    if command == 'add':
        # Проверяем заполнена ли хеш-таблица
        if count == size:
            print("The hash table is full")
        # Если таблица не заполнена полностью вводим ключ
        else:
            print("Enter the key:")
            key = input()
            # Проверяем есть ли уже в хеш-таблице такой ключ
            for index, item in enumerate(h):
                if h[index][1] == key:
                    # Если введенный ключ уже существует выводим сообщение
                    print("This key already exists.")
                    break
            # Если такого ключа нет вводим значение
            else:
                print("Enter the value:")
                value = input()
                # Вычисляем хеш для ключа
                hf = (sum(ord(ch) for ch in key)) * size
                s = str(hf)
                # Из хеша вычисляем индекс вставки ключа
                ind = int(s[0] + s[-1])
                # Проверяем, чтобы индекс был не больше существующих
                while ind >= size:
                    ind = int(ind / 2)
                # Запускаем цикл вставки ключа
                for i in range(size):
                    # Если позиция с найденным индексом уже занята (коллизия) ищем по формуле следующую свободную
                    while h[ind][0] != '':
                        ind = int((ind + 4) - 3)
                        if ind >= size:
                            ind = int(ind * 0)
                    # Если позоция свободна записываем в неё ключ, значение и хеш
                    else:
                        h[ind][0] = hf
                        h[ind][1] = key
                        h[ind][2] = value
                        # Увеличиваем счетчик заполненности хеш-таблицы
                        count = count + 1
                    break
                # Выводим индекс вставленного ключа
                print("Insert in the index:", ind)
                # Выводим хеш-таблицу
                print(h)
    # Команда поиска по ключу или значению
    if command == 'find':
        print("To search by key, enter 1")
        print("To search by key, enter 2")
        find = str(input())
        # Если выбран ввод по ключу
        if find == '1':
            # Вводим ключ
            print("Enter the key")
            key = str(input())
            # Считаем хеш введенного ключа
            hf = (sum(ord(ch) for ch in key)) * size
            # Запускаем цикл поиска по ключу
            for i in range(len(h)):
                # Если хеша нет в существующих выводим сообщение
                if i == len(h) - 1 and hf != h[i][0]:
                    print("No found")
                # Если хеш найден и ключ равен введенному
                if hf == h[i][0] and key == h[i][1]:
                    # Выводим значение, соответствующее данному ключу
                    print("Value:", h[i][2])
        # Если выбран поиск по значению
        if find == '2':
            # Вводим значение
            print("Enter the value")
            value = str(input())
            # Начинаем цикл поиска по значению
            for i in range(len(h)):
                # Если значение не найдено выводим сообщение
                if i == len(h) - 1 and value != h[i][2]:
                    print("No found")
                # Если выполнении равенства выводим ключ, соответствующий значению
                if value == h[i][2]:
                    print("Key:", h[i][1])

    # Команда удаления по ключу или по значению
    if command == 'delete':
        # Проверяем пуста ли хеш-таблица
        if count == 0:
            print("The hash table is empty")
        # Если таблица не пуста продолжаем удаление
        else:
            print("To delete by key, enter 1")
            print("To delete by key, enter 2")
            d = str(input())
            # Удаление по ключу
            if d == '1':
                print("Enter the key")
                dk = str(input())
                # Считаем хеш введенного ключа
                hf = (sum(ord(ch) for ch in dk)) * size
                # Опустошаем позицию с заданным ключом
                for i in range(len(h)):
                    # Если хеш ключа на удаление не найден выводим сообщение
                    if i == len(h) - 1 and hf != h[i][0]:
                        print("No found")
                    # Если хеш найден и ключ равен введенному
                    if hf == h[i][0] and dk == h[i][1]:
                        h[i][0] = ''
                        h[i][1] = ''
                        h[i][2] = ''
                        count = count - 1
                        # Выводим индекс, с которого было удалены значения
                        print("Deleting from the index", i)
                        # Выводим хеш-таблицу
                        print(h)
                        break
            # Удаление по значению
            if d == '2':
                print("Enter the value")
                dv = str(input())
                # Запускаем цикл удаления
                for i in range(size):
                    # Опустошаем позицию с заданным значением
                    if dv == h[i][2]:
                        h[i][0] = ''
                        h[i][1] = ''
                        h[i][2] = ''
                        count = count - 1
                        # Выводим индекс, с которого было удалены значения
                        print("Deleting from the index", i)
                        # Выводим хеш-таблицу
                        print(h)
                        break
                    # Если значение на удаление не найдено выводим сообщение
                    elif i == size - 1 and dv != h[i][1]:
                        print("No found")
    # Команда выхода из программы
    if command == 'exit':
        exit()
