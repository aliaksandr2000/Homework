def  sum_range (start: int, end: int) -> int:

    total = 0
    for i in range (start, end+1):
        total += i
    return total

print(sum_range(start = 7, end = 14))