# Итератор - перебор коллекции
class BookList:
    def __init__(self):
        self.books = []
    
    def add(self, book):
        self.books.append(book)
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        raise StopIteration

# Пример использования
if __name__ == "__main__":
    print("Итератор:")
    library = BookList()
    library.add("Война и мир")
    library.add("Преступление и наказание")
    library.add("Мастер и Маргарита")
    
    for book in library:
        print(f"Книга: {book}")
