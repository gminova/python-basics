filename = input("Enter a filename: ")

with open(filename, 'w+') as f:
    text = f.read()

print(text)
