"""Создание целочисленного списка"""
number = [int(i) for i in input("Enter the numbers and press the space").split()]
#Вывод введенного списка
print (number)
# Суммирование элементов списка
sum = sum(number)
# Вывод результата
print("The amounts of list items:", sum)