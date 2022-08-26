class Triangle:
    def __init__(self, lst_1: list[int]) -> None:
        for side in lst_1:

            if isinstance(side, int or float):
                self.lst_1 = lst_1
            else:
                print('Input correct values (int or float):')
                exit(0)

    def __str__(self):
        return f'{self.lst_1}'

    def sides(self):
        if sorted(self.lst_1)[0] + sorted(self.lst_1)[1] > sorted(self.lst_1)[2]:
            print('Yes')
        else:
            print('No')

sides_1 = [5, 4, 3]
sides_2 = [10,3, 5]

triang_1 = Triangle(sides_1)
triang_2 = Triangle(sides_2)

triang_1.sides()
triang_2.sides()





