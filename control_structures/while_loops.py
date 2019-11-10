i = 1
while i <= 5:
    print(i)
    i = i + 1

print("Finished!")

x = 0
while x <= 20:
    print(x)
    x += 2

y = 0
while True:
    print(y)
    y += 1
    if y >= 5:
        print('break here')
        break

z = 0
while True:
    z += 1
    if z == 2:
        print('skipping 2')
        continue
    if z == 5:
        print('breaking')
        break
