# class Dog:
#     #Атрибут клвсса
#     species  = "Canis Familiaris"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
#
#         # Другой метод экземпляра
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
#     class JackRussellTerrier(Dog):
#         pass
#
#     class Dachshund(Dog):
#         pass
#
#     class Bulldog(Dog):
#         pass
#
# miles = JackRussellTerrier("Miles", 4)
# buddy = Dachshund("Buddy", 9)
# jack = Bulldog("Jack", 3)
# jim = Bulldog("Jim", 5)
#
# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")
# # miles.speak("Woof Woof")
# # 'Miles says Woof Woof'
# # buddy = Dog("Buddy", 9)
# # miles = Dog("Miles", 4)
# print(miles)
class Dog:
    # Атрибут класса
    species = "Canis Familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.breed} and is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4, "Jack Russell Terrier")
buddy = Dachshund("Buddy", 9, "Dachshund")
jack = Bulldog("Jack", 3, "Bulldog")
jim = Bulldog("Jim", 5, "Bulldog")

print(miles)
print(buddy)
print(jack)
print(jim)