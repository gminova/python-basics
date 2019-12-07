file = open('exceptions_and_files/myfile.txt')
content = file.read()
print(content)
file.close()

file = open('exceptions_and_files/myfile.txt')
# print(file.readlines())
for line in file:
    print(line)
file.close()
