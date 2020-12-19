# Создаем класс ресурсов
class Resource:
    # Устанавливаем значение по умолчанию
    __value = 'Free'

    # Функция возврата в исходное состояние
    def reset(self):
        self.__value = 'Free'

    # Функция установки значения соединения
    def setValue(self, str):
        self.__value = 'Using', str

    # Функия получения значения соединения
    def getValue(self):
        return self.__value


# Создаем класс пул объектов 1
class ObjectPool1:
    # Создаем список, в который будем помещать ресурсы, выделенные данным пулом
    __child = list()
    # Устанавливаем тип для соединения
    __connection = None
    # Создаем список для ресурсов
    __resources = list()

    # Создаем экземпляр класса
    def __init__(self):
        if ObjectPool1.__connection != None:
            raise NotImplemented("This is a singleton class.")

    @staticmethod
    def getInstance():
        if ObjectPool1.__connection == None:
            ObjectPool1.__connection = ObjectPool1()
        return ObjectPool1.__connection

    # Функция предоставления соединения
    def getResource(self):
        # Если в данном пуле уже есть свободный ресурс, используем его
        if len(self.__resources) > 0:
            print("Using existing resource.")
            # При этом удаляем его из списка ресурсов
            return self.__resources.pop(0)
        else:
            # Если ресурсов нет, создаем новый
            print("Creating new resource.")
            res = Resource()
            # При создании ресурса добавляем его в список "дочерних" ресурсов,
            # чтобы в дальнейшем предотвратить вмешательства соединений из другого пула
            self.__child.append(res)
            return res

    # Функция возвращения ресурса
    def returnResource(self, resource):
        # Проверяем этим ли пулом был предоставлен ресурс
        if resource in self.__child:
            print("\nReturn in Pool1")
            # Возвращаем русерс
            resource.reset()
            # Добавляем в список свободных ресурсов
            self.__resources.append(resource)
        # Если ресурс был выдан не этим пулом, то выводим сообщение об отсутствии доступа
        else:
            print("\nNot access to Pool1")


# Аналогично первому создаем второй пул
class ObjectPool2:
    __child = list()
    __connection = None
    __resources = list()

    def __init__(self):
        if ObjectPool2.__connection != None:
            raise NotImplemented("This is a singleton class.")

    @staticmethod
    def getInstance():
        if ObjectPool2.__connection == None:
            ObjectPool2.__connection = ObjectPool2()
        return ObjectPool2.__connection

    def getResource(self):
        if len(self.__resources) > 0:
            print("Using existing resource.")
            return self.__resources.pop(0)
        else:
            print("Creating new resource.")
            res = Resource()
            self.__child.append(res)
            return res

    def returnResource(self, resource):
        if resource in self.__child:
            print("\nReturn in Pool")
            resource.reset()
            self.__resources.append(resource)
        else:
            print("\nNot access to Pool")


# Фукнция main
def main():
    # Создаем два пула объектов
    pool1 = ObjectPool1.getInstance()
    pool2 = ObjectPool2.getInstance()
    # Выводим созданные объекты
    print("Pool1", pool1, '\nPool2', pool2)
    # Вызываем функции предоставления ресурса из разных пулов
    one = pool1.getResource()
    two = pool1.getResource()
    three = pool2.getResource()
    # Устанавливаем значения ресурсов
    one.setValue('1')
    two.setValue('2')
    three.setValue('3')
    # Выводим предоставленные ресурсы и их значения
    print("%s = %s" % (one, one.getValue()))
    print("%s = %s" % (two, two.getValue()))
    print("%s = %s" % (three, three.getValue()))
    # Пробуем вернуть в пул 2 пресурс из первого пула
    pool2.returnResource(one)
    # Выводим ресурс и значение ресурса после возврата
    print("%s = %s" % (one, one.getValue()))
    # Возвращаем ресурс из первого пула в первый пул
    pool1.returnResource(two)
    # Выводим ресурс и значение ресурса после возврата
    print("%s = %s" % (two, two.getValue()))
    # Пробуем вернуть в пул 1 пресурс из пула 2
    pool1.returnResource(three)
    # Выводим ресурс и значение ресурса после возврата
    print("%s = %s" % (three, three.getValue()))
    # Вызываем функцию предоставления ресурсов для разных пулов
    one = pool2.getResource()
    two = pool1.getResource()
    three = pool2.getResource()
    # Устанавливаем значения
    one.setValue('4')
    two.setValue('5')
    three.setValue('6')
    # Выводим предоставленные ресурсы и их значения
    print("%s = %s" % (one, one.getValue()))
    print("%s = %s" % (two, two.getValue()))
    print("%s = %s" % (three, three.getValue()))


if __name__ == "__main__":
    main()
