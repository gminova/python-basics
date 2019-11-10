# Python's order of operations is the same as that of normal mathematics:
# parentheses first,
# then exponentiation,
# then multiplication/division,
# and then addition/subtraction.

print(False == False or True, 'must be True')
print(False == (False or True), 'must be False')
print((False == False) or True, 'must be True')
print(False or True, 'must be True')
