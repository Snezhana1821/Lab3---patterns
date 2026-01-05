from abc import ABC, abstractmethod


class House:
    def __init__(self) -> None:
        self.foundation = None
        self.walls = None
        self.roof = None

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


def demo():
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
