squares = [0, 1, 4, 9, 16, 25]
print(squares[0:3])  # [0, 1, 4]
print(squares[:4])  # [0, 1, 4, 9]
print(squares[1:])  # [1, 4, 9, 16, 25]


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])  # [0, 4, 16, 36, 64]
print(squares[2:8:3])  # [4, 25]
print(squares[::-1])  # [81, 64, 49, 36, 25, 16, 9, 4, 1, 0]
