# Мост - разделение
class Device:
    def turn_on(self):
        pass
    
    def turn_off(self):
        pass

class TV(Device):
    def turn_on(self):
        return "Телевизор включен"
    
    def turn_off(self):
        return "Телевизор выключен"

class Radio(Device):
    def turn_on(self):
        return "Радио включено"
    
    def turn_off(self):
        return "Радио выключено"

class Remote:
    def __init__(self, device):
        self.device = device
    
    def press_power(self):
        print(self.device.turn_on())

# Пример использования
if __name__ == "__main__":
    print("Мост:")
    tv_remote = Remote(TV())
    radio_remote = Remote(Radio())
    
    tv_remote.press_power()
    radio_remote.press_power()
