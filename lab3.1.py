# Вводим размер будущей хеш-таблицы
print("Enter the hash table size(enter an integer):")
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
    print("Enter the command(add, exit):")
    command = str(input())
    # Команда добавления ключа
    if command == 'add':
        # Проверяем заполнена ли хеш-таблица
        if count == size:
            print("The hash table is full")
            break
        # Если таблица не заполнена полностью вводим ключ
        else:
            print("Enter the key:")
            key = input()
            # Проверяем есть ли уже в хеш-таблице такой ключ
            for index, item in enumerate(h):
                if h[index][1] == key:
                    print("This key already exists.")
                    break
            # Если такого ключа нет вводим значение
            else:
                print("Enter the value:")
                value = input()
                # Вычисляем хеш для ключа
                hf = (sum(ord(ch) for ch in key))*size
                s = str(hf)
                # Из хеша вычисляем индекс вставки ключа
                ind = int(s[0] + s[-1])
                # Проверяем, чтобы индекс был не больше существующих
                while ind >= size:
                    ind = int(ind * 2/3)
                # Запускаем цикл вставки ключа
                for i in range(size):
                    # Если позиция с найденным индексом уже занята (коллизия) ищем по формуле следующую свободную
                    if h[ind][0] != '':
                        if hf == h[ind][0]:
                            # Определяем как кортеж новые ключ и значение
                            new = tuple([key, value])
                            # Определяем как кортеж уже имеющиеся в позиции ключ и значение
                            old = (h[ind][1], h[ind][2],)
                            # Создаем кортеж кортежей, в котором общий хеш и пары ключ, значение
                            h[ind] = (h[ind][0],)+(old,) + (new,)
                        # Если вычисленный индекс уже занят ключом с другим хешем пересчитываем индекс позиции
                        elif hf != h[ind][0]:
                            ind = int(ind / 2)
                            continue
                    # Если позоция свободна записываем в неё ключ, значение и хеш
                    else:
                        # Увеличиваем счетчик заполненности хеш-таблицы
                        count = count + 1
                        h[ind][0] = hf
                        h[ind][1] = key
                        h[ind][2] = value
                        t = h[ind]
                        h[ind] = tuple(t)
                    break
                # Выводим индекс вставленного ключа
                print("Index:", ind)
                # Выводим хеш-таблицу
                print(h)
    # Команда выхода из программы
    if command == 'exit':
        exit()
