import numpy as np
# Вводим размер матрицы  (количество узлов)
cnt = int(input("PLease enter number of routers : "))
# Создаем рабочие массивы и заполняем их значениями 100 (любое большое число несоразмерное с величиной весов ребер)
x = np.full((cnt, cnt), 100, int)
k = np.full((1, cnt, cnt, cnt), 100, int)


# Функция алгоритма
def upd_routs(o):
    # Создается массив и заполняется значениями 100
    temp = np.full((1, cnt, cnt, cnt), 100)
    # Начинается цикл перебора значений
    for i in range(cnt):
        for j in range(cnt):
            # Проверяется условие равенства i и j
            if i != j:
                # При выполнении условия значения из массива о переносятся в вспомогательный массив temp
                if o[o.shape[0] - 1, i, i, j] == 100:
                    temp[0, i, j, :] = 100
                # Иначе если значение в массиве о не 100 (есть пусть из одного узла в другой) переносится вес ребра
                else:
                    temp[0, i, j, :] = o[o.shape[0] - 1, j, j, :]
            # Если i и j равны запускается цикл перебора по t
            else:
                for t in range(cnt):
                    # При выполнении равенства в массиве temp присваивается значение 0 (зануление главной диагонали
                    # матрицы)
                    if t == i:
                        temp[0, i, i, t] = 0
                    # Иначе присваивается "по умолчанию" значение 100 и запускается цикл поиска кратчайшего пути
                    else:
                        temp[0, i, i, t] = 100
                        for u in range(cnt):
                            # Если при сложении двух значений получается число меньше имеющегося в массиве temp, данное
                            # значение заменяется меньшим
                            if (o[o.shape[0] - 1, i, i, u] + o[o.shape[0] - 1, u, u, t]) < temp[0, i, i, t]:
                                temp[0, i, i, t] = (o[o.shape[0] - 1, i, i, u] + o[o.shape[0] - 1, u, u, t])
    # Если массивы o и temp имеют разную форму и значения, то они объединяются методом concatenate
    if np.array_equal(o[o.shape[0] - 1, :, :, :], temp[0, :, :, :]) is False:
        o = np.concatenate((o, temp))
    # Возвращаем полученный массив
    return o


# Цикл построчного ввода значений матрицы инциндентности
for i in range(cnt):
    s = input("Fill row number %d of the matrix " % (i + 1))
    x[i] = np.fromstring(s, dtype=int, sep=' ')
    # Цикл внесения значений из матрицы инциндентности(массив x) в массив k, который в конце выполнения цикла будет
    # содержать шаги всех итераций
    for j in range(cnt):
        k[0, j, j, :] = x[j, :]
# Цикл выполнения алгоритма
while 1:
    # Определяем переменную как количество строк в массиве k
    before_matrix = k.shape[0]
    # Обращаемся к функции, выполняющий алгоритм поиска кратчайших путей
    k = upd_routs(k)
    # Присваиваем переменной значение - количество строк в массиве k после выполнения алгоритма
    after_matrix = k.shape[0]
    # Сравнение полученных значений, если они равны прекращаем цикл
    if after_matrix == before_matrix:
        break
# Количество итераций определяем как количество строк в массиве k
itr = k.shape
itr = itr[0]
# Цикл выдачи результатов выполнения алгоритма
while 1:
    # Вывод сообщения о количестве итераций и узлов
    print("\n there are %d iterations and %d routers\n" % (itr, cnt))
    print("-------------------------------------------------------------")
    # Ввод номера желаемой итерации алгоритма для просмотра
    iteration_pointer = input(
        "Routing finished successfully...\nPlease enter iteration level you want to take a look at.\n")
    # Вводим номер узла или а для просмотра всех
    router_pointer = input("Enter router number or enter 'a' for overall view.\n")
    # Вывод результата по заданным выше параметрам
    if router_pointer == 'a':
        print(k[int(iteration_pointer) - 1, :, :, :])
    else:
        print(k[int(iteration_pointer) - 1, int(router_pointer) - 1, :, :])
    # Вопрос о продолжении просмотра результата или прекратить программу
    if input("Do you need more report ? (Y/N)").__le__('n'):
        break
