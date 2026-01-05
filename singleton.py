class ConfigManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.environment = "PROD"
        return cls._instance


def demo():
    cfg1 = ConfigManager()
    cfg2 = ConfigManager()
    cfg1.environment = "DEV"
    print("cfg1 env:", cfg1.environment)
    print("cfg2 env:", cfg2.environment)
    print("Это один и тот же объект:", cfg1 is cfg2)
