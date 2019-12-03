print(1)
assert 2 + 2 == 4
print(2)
assert True
temp = -10
assert(temp >= 0), 'Colder than absoulte zero'  # AssertionError
assert 1 + 1 == 3  # AssertionError

# Programmers often place assertions
# at the start of a function to check for valid input,
# and after a function call to check for valid output.
