# filename = input("Enter a filename: ")

# with open(filename) as f:
#     text = f.read()

# print(text)


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


print(count_char('banana', 'n'))

text = 'aaajfjfk'
char = 'j'
perc = 100 * count_char(text, char) / len(text)
print("{0} - {1}%".format(char, round(perc, 2)))
