def max_num(x, y):
    if x >= y:
        return x
    else:
        return y


print(max_num(4, 7))
z = max_num(8, 5)
print(z)


def shortest_string(a, b):
    if len(a) <= len(b):
        return a
    else:
        return b


print(shortest_string('hi', 'bye'))


def add_nums(x, y):
    sum = x + y
    return sum


print(add_nums(5, 6))
