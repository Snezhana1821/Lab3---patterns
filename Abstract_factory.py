from abc import ABC, abstractmethod


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


def demo():
    print("Windows UI:")
    win_app = Application(WindowsFactory())
    win_app.paint()
    print("Mac UI:")
    mac_app = Application(MacFactory())
    mac_app.paint()
