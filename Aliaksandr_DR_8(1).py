class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def car_on(self):
        print('Автомобиль заведен')

    def car_off(self):
        print('Автомобиль заглушен')


    def __str__(self):
        return f'color: {self.color}, type: {self.type}, year: {self.year}'


BMW = Car('black', '530', '2021')
Opel = Car('Green', 'Corsa', '1984')
print(BMW)
print(Opel)
print(BMW.car_off())
print(Opel.car_on())