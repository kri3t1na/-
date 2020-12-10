from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
import xml.etree.ElementTree


# Создаем класс Originator
class Originator:
    _state = None

    # Инициализируем экземпляр класса
    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Начальное состояние: {self._state}")

    # Функция внесения изменений в состояние
    def change(self):
        print("Выполняем изменения в файле.")
        for elem in root.iter('item'):
            elem.text = 'Function change'
        self._state = elem.tag
        print(f"Состояние изменилось на: {self._state}")

    # Функция внесения изменений в состояние
    def do(self):
        # Добавляем новый атрибут
        for elem in root.iter('items'):
            elem.set('name2', 'Function do')
        self._state = elem.tag
        print(f"Состояние изменилось на: {self._state}")

    # Функция сохранения состояния внутри снимка
    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    # Функция восстановления состояния создателя
    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Состояние изменилось на: {self._state}")


# Создаем класс Memento
class Memento(ABC):
    # Абстрактные методы
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


# Создаем класс ConcreteMemento
class ConcreteMemento(Memento):
    # Инициализируем экземпляр класса
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:24]

    # Метод восстановления состояния
    def get_state(self) -> str:
        return self._state

    # Функция отображения названия состояния
    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:10]})"

    # Функция отображения даты создания снимка
    def get_date(self) -> str:
        return self._date


# Создаем класс Caretaker
class Caretaker:
    # Инициализируем экземпляр класса
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    # Делаем резервную копию состояния
    def backup(self) -> None:
        print("\nСохраняем состояние.")
        self._mementos.append(self._originator.save())

    # Метод отмены состояния
    def undo(self) -> None:
        if not len(self._mementos):
            return
        memento = self._mementos.pop()
        print(f"Восстановление состояния: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    # Функция отображения сохраненных состояний
    def show_state(self) -> None:
        print("Список сохраненных состояний:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    # Строим дерево элементов файла items.xml
    doc = xml.etree.ElementTree.parse('items.xml')
    # Находим корневой элемент
    root = doc.getroot()
    # Определяем переменные как классы Originator и Caretaker
    originator = Originator(root.tag)
    caretaker = Caretaker(originator)
    # Сохраняем состояние
    caretaker.backup()
    # Изменяем состояние
    originator.change()
    caretaker.backup()
    # Изменяем состояние
    originator.do()
    # Выводим список сохраненных состояний
    print()
    caretaker.show_state()
    # Возвращаемся в последнее состояние
    print("\nОткатимся до предыдущего состояния.\n")
    caretaker.undo()
    print("\nОткатимся еще раз.\n")
    caretaker.undo()
