class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def move_1(self):
        print('Автомобиль заведен')

    def move_2(self):
        print('Автомобиль заглушен')


    def __str__(self):
        return f'color: {self.color}, type: {self.type}, year: {self.year}'


BMW = Car('black', '530', '2021')
Opel = Car('Green', 'Corsa', '1984')
print(BMW)
print(Opel)
print(BMW.move_1())
print(Opel.move_2())