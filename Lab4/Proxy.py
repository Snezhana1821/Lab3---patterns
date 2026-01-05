# Прокси - контролирует доступ
class RealFile:
    def __init__(self, filename):
        self.filename = filename
        print(f"Загружаем файл {filename}...")
    
    def read(self):
        return f"Содержимое {self.filename}"

class FileProxy:
    def __init__(self, filename):
        self.filename = filename
        self._real_file = None
    
    def read(self):
        if self._real_file is None:
            self._real_file = RealFile(self.filename)
        return self._real_file.read()

# Пример использования
if __name__ == "__main__":
    print("Прокси:")
    proxy = FileProxy("report.txt")
    print(proxy.read())
    print(proxy.read())
