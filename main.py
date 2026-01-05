from abc import ABC, abstractmethod


def main():
    print("=== Singleton ===")
    demo_singleton()

    print("\n=== Factory Method ===")
    demo_factory_method()

    print("\n=== Abstract Factory ===")
    demo_abstract_factory()

    print("\n=== Builder ===")
    demo_builder()


class ConfigManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.environment = "PROD"
        return cls._instance


def demo_singleton():
    cfg1 = ConfigManager()
    cfg2 = ConfigManager()
    cfg1.environment = "DEV"
    print("cfg1 env:", cfg1.environment)
    print("cfg2 env:", cfg2.environment)
    print("Это один и тот же объект:", cfg1 is cfg2)


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"[CONSOLE] {message}")


class FileLogger(Logger):
    def log(self, message: str) -> None:
        print(f"[FILE] {message}")


class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

    def log_message(self, message: str) -> None:
        logger = self.create_logger()
        logger.log(message)


class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()


class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()


def demo_factory_method():
    console_factory = ConsoleLoggerFactory()
    file_factory = FileLoggerFactory()
    console_factory.log_message("Сообщение в консоль")
    file_factory.log_message("Сообщение в файл")


class Button(ABC):
    @abstractmethod
    def paint(self) -> None:
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self) -> None:
        pass


class WindowsButton(Button):
    def paint(self) -> None:
        print("Рисуем кнопку в стиле Windows")


class MacButton(Button):
    def paint(self) -> None:
        print("Рисуем кнопку в стиле Mac")


class WindowsCheckbox(Checkbox):
    def paint(self) -> None:
        print("Рисуем чекбокс в стиле Windows")


class MacCheckbox(Checkbox):
    def paint(self) -> None:
        print("Рисуем чекбокс в стиле Mac")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class Application:
    def __init__(self, factory: GUIFactory) -> None:
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self) -> None:
        self.button.paint()
        self.checkbox.paint()


def demo_abstract_factory():
    print("Windows UI:")
    win_app = Application(WindowsFactory())
    win_app.paint()
    print("Mac UI:")
    mac_app = Application(MacFactory())
    mac_app.paint()


class House:
    def __init__(self) -> None:
        self.foundation: str | None = None
        self.walls: str | None = None
        self.roof: str | None = None

    def __repr__(self) -> str:
        return f"House(foundation={self.foundation}, walls={self.walls}, roof={self.roof})"


class HouseBuilder(ABC):
    @abstractmethod
    def build_foundation(self) -> None:
        pass

    @abstractmethod
    def build_walls(self) -> None:
        pass

    @abstractmethod
    def build_roof(self) -> None:
        pass

    @abstractmethod
    def get_result(self) -> House:
        pass


class WoodenHouseBuilder(HouseBuilder):
    def __init__(self) -> None:
        self._house = House()

    def build_foundation(self) -> None:
        self._house.foundation = "ленточный фундамент"

    def build_walls(self) -> None:
        self._house.walls = "деревянные стены"

    def build_roof(self) -> None:
        self._house.roof = "двускатная крыша из черепицы"

    def get_result(self) -> House:
        return self._house


class BrickHouseBuilder(HouseBuilder):
    def __init__(self) -> None:
        self._house = House()

    def build_foundation(self) -> None:
        self._house.foundation = "монолитная плита"

    def build_walls(self) -> None:
        self._house.walls = "кирпичные стены"

    def build_roof(self) -> None:
        self._house.roof = "плоская крыша"

    def get_result(self) -> House:
        return self._house


class HouseDirector:
    def __init__(self, builder: HouseBuilder) -> None:
        self._builder = builder

    def construct_house(self) -> None:
        self._builder.build_foundation()
        self._builder.build_walls()
        self._builder.build_roof()


def demo_builder():
    wooden_builder = WoodenHouseBuilder()
    director1 = HouseDirector(wooden_builder)
    director1.construct_house()
    wooden_house = wooden_builder.get_result()
    print("Деревянный дом:", wooden_house)

    brick_builder = BrickHouseBuilder()
    director2 = HouseDirector(brick_builder)
    director2.construct_house()
    brick_house = brick_builder.get_result()
    print("Кирпичный дом:", brick_house)


if __name__ == "__main__":
    main()
