# Адаптер - совмещает интерфейсы
class OldSocket:
    def old_connect(self):
        return "Подключение через старый разъем"

class NewSocket:
    def new_connect(self):
        return "Подключение через новый разъем"

class Adapter:
    def __init__(self, old_socket):
        self.old_socket = old_socket
    
    def new_connect(self):
        # Адаптируем вызов
        return self.old_socket.old_connect() + " (адаптировано)"

# Пример использования
if __name__ == "__main__":
    print("Адаптер:")
    new = NewSocket()
    old = OldSocket()
    adapter = Adapter(old)
    
    print(new.new_connect())
    print(adapter.new_connect())
