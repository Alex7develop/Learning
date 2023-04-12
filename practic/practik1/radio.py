class Radio:
    def __init__(self, volume, frequency, power):
        self.volume = volume
        self.frequency = frequency
        self.power = power

    def get_volume(self):
        return 'Громкость: ' + self.volume

    def get_frequency(self):
        return 'Частота волны: ' + str(self.frequency)

    def get_power(self):
        return 'Включить или выключить: ' + str(self.power)


class Employee(Radio):
    def __init__(self, volume, frequency, power):
        super().__init__(volume, frequency, power)


test = Employee('Громко', 101, 'Включено')

print(test.get_power())

test1 = Radio('Громко', 103, 'Включено')
test2 = Radio('Тихо', 102, 'Выключено')
test3 = Radio('Громко', 108, 'Включено')
print(test1.get_volume())
print(test1.get_frequency())