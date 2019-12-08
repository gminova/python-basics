squares = {1: 1, 2: 4, 3: "error", 4: 16, }
squares[8] = 64
squares[3] = 9
print(squares)


nums = {
    1: 'one',
    2: 'two'
}

print(1 in nums)
print('one' in nums)
print(4 not in nums)
print(nums.get(1))
print(nums.get('blah', 'blah not in nums'))
