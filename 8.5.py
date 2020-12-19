from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Создаем класс Component
class Component(ABC):

    # Декораторы
    @property
    def level_up(self) -> Component:
        return self._level_up

    @level_up.setter
    def level_up(self, level_up: Component):
        self._level_up = level_up

    # Функция добавления
    def add(self, component: Component) -> None:
        pass

    # Функция удаления
    def remove(self, component: Component) -> None:
        pass

    # Абстрактный метод
    @abstractmethod
    def operation(self) -> str:
        pass


# Создаем класс компоновщика
class Composite(Component):
    # Инициализируем экземпляр класса
    def __init__(self) -> None:
        self._level_down: List[Component] = []

    # Функция добавления компонента объектом контейнера в список вложенных
    def add(self, component: Component) -> None:
        self._level_down.append(component)
        component.level_up = self

    # Функция удаления компонента объектом контейнера в список вложенных
    def remove(self, component: Component) -> None:
        self._level_down.remove(component)
        component.level_up = None

    # Функция обхода контейнером всех потомков
    def operation(self) -> str:
        results = []
        for level_d in self._level_down:
            results.append(level_d.operation())
        return f"({'+'.join(results)})"


# Создадим класс Воин
class Warrior(Component):
    def operation(self) -> str:
        return "Warrior"


# Создаем класс Рыцари
class Knights(Component):
    # Создаем экземпляр класса
    def __init__(self) -> None:
        self._level_down: List[Component] = []

    # Функция добавления компонента объектом контейнера в список вложенных
    def add(self, component: Component) -> None:
        self._level_down.append(component)
        component.level_up = self

    # Функция удаления компонента объектом контейнера в список вложенных
    def remove(self, component: Component) -> None:
        self._level_down.remove(component)
        component.level_up = None

    # Функция обхода контейнером всех потомков
    def operation(self) -> str:
        results = []
        for level_d in self._level_down:
            results.append(level_d.operation())
        return f"Squad of Knights({'+'.join(results)})"


# Создаем класс Гидры
class Hydras(Component):
    # Инициализируем экземпляр класса
    def __init__(self) -> None:
        self._level_down: List[Component] = []

    # Функция добавления компонента объектом контейнера в список вложенных
    def add(self, component: Component) -> None:
        self._level_down.append(component)
        component.level_up = self

    # Функция удаления компонента объектом контейнера в список вложенных
    def remove(self, component: Component) -> None:
        self._level_down.remove(component)
        component.level_up = None

    # Функция обхода контейнером всех потомков
    def operation(self) -> str:
        results = []
        for level_d in self._level_down:
            results.append(level_d.operation())
        return f"Squad of Hydra({'+'.join(results)})"


# Создаем класс Драконы
class Dragons(Component):
    # Инициализируем экземпляр класса
    def __init__(self) -> None:
        self._level_down: List[Component] = []

    # Функция добавления компонента объектом контейнера в список вложенных
    def add(self, component: Component) -> None:
        self._level_down.append(component)
        component.level_up = self

    # Функция удаления компонента объектом контейнера в список вложенных
    def remove(self, component: Component) -> None:
        self._level_down.remove(component)
        component.level_up = None

    # Функция обхода контейнером всех потомков
    def operation(self) -> str:
        results = []
        for level_d in self._level_down:
            results.append(level_d.operation())
        return f"Squad of Dragons({'+'.join(results)})"


# Создаем класс Циклопы
class Cyclops(Component):
    # Инициализируем экземпляр класса
    def __init__(self) -> None:
        self._level_down: List[Component] = []

    # Функция добавления компонента объектом контейнера в список вложенных
    def add(self, component: Component) -> None:
        self._level_down.append(component)
        component.level_up = self

    # Функция удаления компонента объектом контейнера в список вложенных
    def remove(self, component: Component) -> None:
        self._level_down.remove(component)
        component.level_up = None

    # Функция обхода контейнером всех потомков
    def operation(self) -> str:
        results = []
        for level_d in self._level_down:
            results.append(level_d.operation())
        return f"Squad of cyclops({'+'.join(results)})"


# Создаем класс Кентавры
class Centaurs (Component):
    # Инициализируем экземпляр класса
    def __init__(self) -> None:
        self._level_down: List[Component] = []

    # Функция добавления компонента объектом контейнера в список вложенных
    def add(self, component: Component) -> None:
        self._level_down.append(component)
        component.level_up = self

    # Функция удаления компонента объектом контейнера в список вложенных
    def remove(self, component: Component) -> None:
        self._level_down.remove(component)
        component.level_up = None

    # Функция обхода контейнером всех потомков
    def operation(self) -> str:
        results = []
        for level_d in self._level_down:
            results.append(level_d.operation())
        return f"Squad of centaurs({'+'.join(results)})"


# Создаем класс Минотавры
class Minotaurs(Component):
    # Инициализируем экземпляр класса
    def __init__(self) -> None:
        self._level_down: List[Component] = []

    # Функция добавления компонента объектом контейнера в список вложенных
    def add(self, component: Component) -> None:
        self._level_down.append(component)
        component.level_up = self

    # Функция удаления компонента объектом контейнера в список вложенных
    def remove(self, component: Component) -> None:
        self._level_down.remove(component)
        component.level_up = None

    # Функция обхода контейнером всех потомков
    def operation(self) -> str:
        results = []
        for level_d in self._level_down:
            results.append(level_d.operation())
        return f"Squad of minotaurs({'+'.join(results)})"


# Создаем класс Орков
class Orcs(Component):
    # Инициализируем экземпляр класса
    def __init__(self) -> None:
        self._level_down: List[Component] = []

    # Функция добавления компонента объектом контейнера в список вложенных
    def add(self, component: Component) -> None:
        self._level_down.append(component)
        component.level_up = self

    # Функция удаления компонента объектом контейнера в список вложенных
    def remove(self, component: Component) -> None:
        self._level_down.remove(component)
        component.level_up = None

    # Функция обхода контейнером всех потомков
    def operation(self) -> str:
        results = []
        for level_d in self._level_down:
            results.append(level_d.operation())
        return f"Squad of orcs({'+'.join(results)})"


# Создаем класс эльфов
class Elfs(Component):
    # Инициализируем экземпляр класса
    def __init__(self) -> None:
        self._level_down: List[Component] = []

    # Функция добавления компонента объектом контейнера в список вложенных
    def add(self, component: Component) -> None:
        self._level_down.append(component)
        component.level_up = self

    # Функция удаления компонента объектом контейнера в список вложенных
    def remove(self, component: Component) -> None:
        self._level_down.remove(component)
        component.level_up = None

    # Функция обхода контейнером всех потомков
    def operation(self) -> str:
        results = []
        for level_d in self._level_down:
            results.append(level_d.operation())
        return f"Squad of elfs({'+'.join(results)})"


# Клиентский код
def client_code(component: Component) -> None:
    print(f"Army: {component.operation()}", end="")


if __name__ == "__main__":
    # Определяем переменную tree как класс Сomposite
    Army = Composite()
    # Операции добавления файлов в структуру
    Army.add(Warrior())
    squad1 = Elfs()
    squad1.add(Centaurs())
    squad1.add(Minotaurs())
    subsquad1 = Cyclops()
    subsquad2 = Warrior()
    subsquad1.add(subsquad2)
    squad1.add(subsquad1)
    squad2 = Knights()
    squad2.add(Dragons())
    Army.add(squad1)
    Army.add(squad2)
    # Выводим получившуюся структуру дерева
    client_code(Army)
    Army.remove(squad1)
    # Выводим получившуюся структуру дерева
    print("\nRemoving the squad1")
    client_code(Army)
    # Создадим переменную класса Воин и убедимся,
    # что Воин является простой(не может включать другие отряды) наименьшей единицей
    squad3 = Warrior()
    squad3.add(Hydras())
    Army.add(squad3)
    print('\nCheck that the warrior is a simple element')
    client_code(Army)
