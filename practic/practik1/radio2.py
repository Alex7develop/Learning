class Radio:
    def __init__(self, volume=0, frequency=0, is_on=False):
        self.volume = volume
        self.frequency = frequency
        self.is_on = is_on

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency

    def is_radio_on(self):
        return self.is_on

    def turn_radio_on(self):
        self.is_on = True

    def turn_radio_off(self):
        self.is_on = False

my_radio = Radio()

my_radio.set_volume(50)
my_radio.set_frequency(100.5)
my_radio.turn_radio_on()

print("Громкость:", my_radio.get_volume())
print("Частота:", my_radio.get_frequency())
print("Радио включено", my_radio.is_radio_on())

my_radio.turn_radio_off()
print("Радио выключено", my_radio.is_radio_on())