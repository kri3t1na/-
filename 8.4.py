# Создаем класс стратегия обучения
class StrategyTeach:
    def __init__(self, func=None):
        if func:
            self.way = func


# Функция, определяющая способы обучения студента
def univer_way():
    print("Форма обучения: очная, очно-заочная, заочная, экстернат")


# Функция, определяющая способы обучения школьника
def school_way():
    print("Форма обучения: очная, очно-заочная, заочная, семейное(1-9), самообразование(10-11)")


# Создадим класс состояний образования
class EducatState(object):
    name = "state"
    possible = []

    # Функция, определяющая способ обучения для каждого состояния
    def way_learn(self, state):
        if state.name == str('школьник'):
            StrategyTeach(school_way())
        else:
            StrategyTeach(univer_way())

    # Функция, осуществляющая переход между состояниями
    def switch(self, state):
        # Условие проверки перехода состояния
        if state.name in self.possible:
            # Если в возможных переходах состояний есть указанное
            print('\nИз состояния', self, ' можно перейти в состояние', state.name)
            # Обращаемся к функции определения способа обучения
            self.way_learn(state)
            # Переходим в указанное состояние
            self.__class__ = state
        # Если указано состояние, в котором мы уже находимся
        elif state.name == str(self):
            print('\nВы уже в состоянии', self)
            # Указываем способы обучения
            self.way_learn(state)
        # Если в возможных состояниях нет указанного
        else:
            print('\nИз состояния', self, 'невозможно перейти в состояние', state.name)

    # Функция строкового представления объекта
    def __str__(self):
        return self.name


# Создаем класс школьник
class SchoolBoy(EducatState):
    name = "школьник"
    # Указываем возможные состояния перехода
    possible = ['студент']


# Создаем класс студент
class Student(EducatState):
    name = "студент"
    # Указываем возможные состояния перехода
    possible = ['аспирант']


# Создаем класс аспирант
class GraduateStud(EducatState):
    name = "аспирант"
    # Указываем возможные состояния перехода
    possible = ['работник']


# Создаем класс Учащийся
class Learner(object):
    # Создаем экземпляр класса
    def __init__(self):
        # Указываем исходное состояние
        self.state = SchoolBoy()

    # Функция перехода в состояние
    def change(self, state):
        """ Change state """
        self.state.switch(state)


if __name__ == "__main__":
    # Опеределяем переменную как класс Учащийся
    learner = Learner()
    # Укажем переход в состояние школьник
    learner.change(SchoolBoy)
    # Укажем переход в состояние студент
    learner.change(Student)
    # Укажем переход в состояние школьник
    learner.change(SchoolBoy)
    # Укажем переход в состояние аспирант
    learner.change(GraduateStud)
