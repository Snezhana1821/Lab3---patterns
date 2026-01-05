# Цепочка - обработка по очереди
class Handler:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.next = None
    
    def set_next(self, handler):
        self.next = handler
        return handler
    
    def process(self, amount):
        if amount <= self.limit:
            return f"{self.name} обработал запрос на {amount}"
        elif self.next:
            return self.next.process(amount)
        else:
            return f"Никто не может обработать {amount}"

# Пример использования
if __name__ == "__main__":
    print("Цепочка обязанностей:")
    manager = Handler("Менеджер", 1000)
    director = Handler("Директор", 5000)
    ceo = Handler("Гендиректор", 10000)
    
    manager.set_next(director).set_next(ceo)
    
    print(manager.process(500))
    print(manager.process(3000))
    print(manager.process(8000))
    print(manager.process(20000))
