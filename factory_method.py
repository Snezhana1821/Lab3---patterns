from abc import ABC, abstractmethod


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


def demo():
    console_factory = ConsoleLoggerFactory()
    file_factory = FileLoggerFactory()
    console_factory.log_message("Сообщение в консоль")
    file_factory.log_message("Сообщение в файл")
