num_set = {1, 2, 3}
word_set = set(['spam', 'eggs', 'tomatoes'])
print(3 in num_set)
print('eggs' not in word_set)

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

# Sets can be combined using mathematical operations.
# The union operator | combines two sets to form a new one containing items in either.
# The intersection operator & gets items only in both.
# The difference operator - gets items in the first set but not in the second.
# The symmetric difference operator ^ gets items in either set, but not both.
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
