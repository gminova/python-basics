print(1 == 1 and 2 == 2, 'must be True')
print(1 == 1 and 3 == 2, 'must be False')
print(1 != 1 and 2 != 2, 'must be False')
print(2 < 1 and 2 > 1, 'must be False')

if (1 == 1) and (2 + 2 > 3):
    print(True)
else:
    print(False)


if (1 == 1) or (2 == 2):
    print(True)
else:
    print(False)

age = 16
cash = 20
if age > 18 or cash > 10:
    print('Welcome')
else:
    print('Come back later')

print(not 1 == 1, 'must be False')
print(not 3 > 5, 'must be True')
