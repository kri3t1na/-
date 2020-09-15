"""Создание строки-образца"""
pas_obr = "P@$$w0rd"
#Создание цилка для сравнения введенного пароля и образца
while True:
    # Ввод пароля пользователем
    pas = str(input("Enter the password:"))
    #Условие сравнения паролей
    if pas_obr == pas:
        print("You entered the correct password")
        break
    else:
        print("You entered an invalid password")
