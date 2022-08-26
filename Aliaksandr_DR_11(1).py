class User:
    def __init__(self, name, surname, age, country, profession) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.profession = profession

    def get_email(self):
        email = f'{self.name}.{self.surname}@mail.com'
        return email
    def get_birth_year(self):
        birth_year = 2022 - int(self.age)
        return birth_year
    @staticmethod
    def doktor():
        doctor = User('name', 'surname',12, 'doctor')
        return doctor

    @staticmethod
    def policeman():
        policeman = User('name', 'surname', 12, 'policeman')
        return policeman

    @staticmethod
    def teacher():
        teacher = User('name', 'surname', 12, 'teacher')
        return teacher
