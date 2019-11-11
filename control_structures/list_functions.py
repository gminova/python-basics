nums = [1, 2, 3]
# append method
nums.append(4)
print('original', nums)
nums.append([5])
print('append [5]', nums)
# len function
print('length', len(nums))
# insert method
index = 0
nums.insert(index, 'zero')
print('insert zero at index 0', nums)
# index method - finds first occurance of a list
print('index of 3', nums.index(3))
print('max num', max(nums))
print('min num', min(nums))
print('occurances of 1', nums.count(1))
print('remove zero', nums.remove('zero'), 'nums', nums)
print('reverse', nums.reverse(), 'nums', nums)
