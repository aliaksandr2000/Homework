class Clothes:
    __clothes_count = 0
    def __init__(self,size: int, style: str) -> None:
        self.size = size
        self.style = style
        Clothes.__clothes_count += 1
    @classmethod
    def get_clothes_count(cls):
        return cls.__clothes_count

class Womens_clothing(Clothes):
    def __init__(self, size: int, style: str, dress: str, shirt: str) -> None:
        super().__init__(size, style)
        self.dress = dress
        self.shirt = shirt

    def womens_clothing_sizes(self):
        if self.size <= 44:
            print('Women size')
        elif self.size == 0:
            print('Error')

class Men_clothing(Womens_clothing):
    def __init__(self, size, style, shirt, jeans: str, t_shirt: str) -> None:
        super().__init__(size, style)
        Womens_clothing.shirt = shirt
        self.jeans = jeans
        self.t_shirt = t_shirt

    def mens_clothing_sizes(self):
        if self.size > 44 < 62:
            print('Men size')

class Kids_clothing(Clothes):
    def __init__(self, size, style, dress, shirt, jeans, t_shirt, shorts: str, jacket: str) -> None:
        super().__init__(size, style)
        Womens_clothing.dress = dress
        Womens_clothing.shirt = shirt
        Men_clothing.jeans = jeans
        Men_clothing.t_shirt = t_shirt
        self.shorts = shorts
        self.jacket = jacket
    def kids_clothing_sizes(self):
        if self.size == 92 or 98 or 104 or 110 or 116 or 122 or 128 or 134 or 140:
            print('Kids size')

class Big_sizes(Clothes):
    def __init__(self, size, style, dress, shirt, jeans, t_shirt, shorts, jacket, hoodie: str, jeans_big: float, t_shirt_big: float) -> None:
        super().__init__(size, style)
        Womens_clothing.dress = dress
        Womens_clothing.shirt = shirt
        Men_clothing.jeans = jeans
        Men_clothing.t_shirt = t_shirt
        Kids_clothing.shorts = shorts
        Kids_clothing.jacket = jacket
        self.jeans_big = jeans_big
        self.t_shirt_big = t_shirt_big
    def big_clothing_size(self):
        if self.jeans_big >= 63:
            print('Big sizes')

    def __str__(self):
        return f'{self.size}, {self.style}, {self.dress}, {self.jeans}, {self.t_shirt}, {self.shorts}, {self.jacket}, {self.jeans_big}, {self.t_shirt_big}'


clothing_model_1 = Clothes(90, 'Casual' )
print(clothing_model_1)
print(Clothes.get_clothes_count())




