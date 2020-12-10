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


# Создадим класс File
class File(Component):
    def operation(self) -> str:
        return "File"


# Создаем класс Composite
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
        return f"Directory({'+'.join(results)})"


# Клиентский код
def client_code(component: Component) -> None:
    print(f"Structure: {component.operation()}", end="")


if __name__ == "__main__":
    # Определяем переменную tree как класс Сomposite
    tree = Composite()
    # Операции добавления файлов в структуру
    tree.add(File())
    level1 = Composite()
    level1.add(File())
    level1.add(File())
    subdir = Composite()
    sublevel = File()
    subdir.add(sublevel)
    level1.add(subdir)
    level2 = Composite()
    level2.add(File())
    tree.add(level1)
    tree.add(level2)
    # Выводим получившуюся структуру дерева
    client_code(tree)
    print("\n")
    tree.remove(level1)
    # Выводим получившуюся структуру дерева
    client_code(tree)
    print("\n")
