# Создаем класс Рецепт как одиночку
class Prescription(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Prescription, cls).__new__(cls)
        return cls.instance


# Определяем переменную как класс Рецепт
rec = Prescription()
# Выводим сообщение о том, что Рецепт создан и объект
print("Prescription issued\n", rec)
# Спрашиваем сколько прошло времени со дня выписки рецепта
print("How many days have passed since the prescription was issued?")
# Вводим количество дней
day = int(input())
# Если прошло больше 5 дней продлеваем(выписываем) этот же рецепт еще раз
if day > 5:
    new_rec = rec
    print("The prescription issued again\n", new_rec)
else:
    print("The previous recipe is still valid")
