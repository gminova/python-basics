nums = [7, 7, 7, 7]
nums[0] = 4
print(nums[0])

ints = [1, 2, 3]
print(ints + [4, 5, 6])
print(ints * 3)

foods = ['spam', 'eggs', 'bacon', 'spam' 'mushrooms']
print('spam' in foods, 'must be True')
print('eggs' in foods, 'must be True')
print('dog' in foods, 'must be False')

print('defined' in 'undefined', 'must be True')

my_nums = [1, 2, 3]
print(not 4 in my_nums)
print(4 not in my_nums)
print(not 3 in my_nums)
print(3 not in my_nums)

letters = ['a', 'b', 'z']
if 'z' in letters:
    print('Yes')
