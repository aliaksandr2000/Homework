nums = [1, 5, 2, 1, 3, 5, 8]
 # counter = [2, 2, 1, 2, 1, 2, 1]
duplicate = [x for i, x in enumerate(nums) if i != nums.index(x)]
print(duplicate)