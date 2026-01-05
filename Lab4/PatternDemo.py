from Strategy import Travel, Car, Train, Plane
from Responsibility_chain import Handler
from Iterator import BookList
from Proxy import FileProxy
from Adapter import OldSocket, NewSocket, Adapter
from Bridge import TV, Radio, Remote

print("=== ДЕМОНСТРАЦИЯ 6 ПАТТЕРНОВ ===")
print()

# 1. Стратегия
print("1. СТРАТЕГИЯ")
print("-" * 30)
trip1 = Travel(Car())
trip2 = Travel(Train())
trip3 = Travel(Plane())

print(f"   Москва-Санкт-Петербург (400 км):")
print(f"   • {trip1.travel(400)}")
print(f"   • {trip2.travel(400)}")
print(f"   • {trip3.travel(400)}")
print()
# 2. Цепочка обязанностей
print("2. ЦЕПОЧКА ОБЯЗАННОСТЕЙ")
print("-" * 30)
manager = Handler("Менеджер", 1000)
director = Handler("Директор", 5000)
ceo = Handler("Гендиректор", 10000)

manager.set_next(director)
director.set_next(ceo)

requests = [500, 3000, 8000, 20000]
for amount in requests:
    result = manager.process(amount)
    print(f"   Запрос на {amount} руб.: {result}")
print()

# 3. Итератор
print("3. ИТЕРАТОР")
print("-" * 30)
library = BookList()
library.add("Война и мир")
library.add("Преступление и наказание")
library.add("Мастер и Маргарита")

print("   Книги в библиотеке:")
for book in library:
    print(f"   • {book}")
print()
# 4. Прокси
print("4. ПРОКСИ")
print("-" * 30)
proxy = FileProxy("report.txt")
print(f"   Первое чтение: {proxy.read()}")
print(f"   Второе чтение: {proxy.read()} (из кэша)")
print()

# 5. Мост
print("5. МОСТ")
print("-" * 30)
tv_remote = Remote(TV())
radio_remote = Remote(Radio())

print("   Телевизор: ", end="")
tv_remote.press_power()
print("   Радио: ", end="")
radio_remote.press_power()
print()

# 6. Адаптер
print("6. АДАПТЕР")
print("-" * 30)
new_socket = NewSocket()
old_socket = OldSocket()
adapter = Adapter(old_socket)

print(f"   Новый разъем: {new_socket.new_connect()}")
print(f"   Старый через адаптер: {adapter.new_connect()}")
print()

print("=" * 40)
print("✅ ВСЕ ПАТТЕРНЫ РАБОТАЮТ КОРРЕКТНО")
print("=" * 40)
