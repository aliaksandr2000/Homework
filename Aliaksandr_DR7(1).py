def Leonardo_Pisano(num: int) -> int:
    num_1 = 0
    num_2 = 1
    for i in range(num):
        num_2 = num_1 + num_2
        num_1 = num_2 - num_1
        print(num_1, end=' ')


Leonardo_Pisano(5)