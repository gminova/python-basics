def add_five(x):
    return x + 5


nums = [1, 2, 3]
result = list(map(add_five, nums))
print(result)
