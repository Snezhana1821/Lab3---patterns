# Стратегия - разные алгоритмы
class Travel:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def travel(self, distance):
        return self.strategy.calculate(distance)

class Car:
    def calculate(self, distance):
        return f"На машине: {distance/80:.1f} часов"

class Train:
    def calculate(self, distance):
        return f"На поезде: {distance/120:.1f} часов"

class Plane:
    def calculate(self, distance):
        return f"На самолете: {distance/800:.1f} часов"

# Пример использования
if __name__ == "__main__":
    print("Стратегия:")
    trip1 = Travel(Car())
    trip2 = Travel(Train())
    trip3 = Travel(Plane())
    print(trip1.travel(400))
    print(trip2.travel(400))
    print(trip3.travel(400))
