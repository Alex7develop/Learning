class Test:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return 'Меня зовут ' + self.name

    def get_age(self):
        return 'Мне уже ' + str(self.age)

    def hello(self):
        return 'Привет! ' + self.get_name() + ' ' + self.get_age()


class Employee(Test):
    def __init__(self, name, age, post):
        super().__init__(name, age)
        self.post = post

    def get_rank(self):
        return 'Должность: ' + self.post


director = Employee('Михаил', 55, 'директор')
print(director.hello())
print(director.get_rank())

test1 = Test('Вася', 35)
test2 = Test('Макс', 29)
test3 = Test('Leo', 17)
print(test1.get_name())
print(test1.get_age())
print(test1.hello())
print(test2.hello())
print(test3.hello())
