import random

# Создаем список возможных значений карт
cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Рандомно перемешиваем значения списка
random.shuffle(cards)
# "Раздаем" карты первому игроку
first = cards[0:5]
# Р"Раздаем" карты второму игроку
second = cards[5:10]
# Выводим розданные карты
print("Cards of first player", first)
print("Cards of second player", second)
# Устанавливаем счетчик ходов на 0
moves = 0
# Начинаем игровой цикл
while True:
    # Выбираем первую карту у первого игрока
    card_f = first.pop(0)
    # Выбираем первую карту у второго игрока
    card_s = second.pop(0)
    # Начинаем проверку условий игры
    if card_f == 0 and card_s == 9:
        # Первый игрок забирает карты себе
        first += [card_f, card_s]
        # Увеличиваем счетчик ходов
        moves += 1

    if card_s == 0 and card_f == 9:
        second += [card_f, card_s]
        moves += 1

    if card_f > card_s:
        first += [card_f, card_s]
        moves += 1

    if card_s > card_f:
        second += [card_f, card_s]
        moves += 1
    # Проверяем наличие карту первого игрока
    if len(first) == 0:
        # Если карт нет, то игрок проиграл, выводи количество ходов]
        print("Won second player. Amount of moves:", moves)
        # Завершаем игру
        break
    # Проверяем наличие карт у второго игрока
    if len(second) == 0:
        print("Won first player. Amount of moves: ", moves)
        break
    # Проверка количества ходов
    if moves == 1000000:
        # Если ходов больше допустимого выводится сообщение и игра прекращается
        print("To long")
        break