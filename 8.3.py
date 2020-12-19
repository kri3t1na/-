# Создаем класс магазин цветов
class FlowerStore:
    def operation(self) -> str:
        pass


# Создаем класс Декоратор
class Decorator(FlowerStore):
    _component: FlowerStore = None

    # Создаем экземпляр класса
    def __init__(self, component: FlowerStore) -> None:
        self._component = component

    # Декоратор, делегирующий работу обернутому компоненту
    @property
    def component(self) -> str:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


# Создаем класс букет
class Bouquet(FlowerStore):
    # Вызываем родительскую реализацию операции
    def operation(self) -> str:
        return "Bouquet"


# Создаем класс упаковки(оберточная бумага)
class Packaging(Decorator):
    # Вызываем родительскую реализацию операции
    def operation(self) -> str:
        return f"Packaging({self.component.operation()})"


# Создаем класс лента
class Feed(Decorator):
    # Вызываем родительскую реализацию операции
    def operation(self) -> str:
        return f"Feed({self.component.operation()})"


# Функция клиентского кода, работающая со всеми объектами
def client_code(component: FlowerStore) -> None:
    print(f"Order: {component.operation()}", end="")


if __name__ == "__main__":
    bouquet = Bouquet()
    decorator1 = Packaging(bouquet)
    decorator2 = Feed(decorator1)
    print("Completed order:")
    client_code(decorator2)
