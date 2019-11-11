words = ['hello', 'world', 'spam', 'eggs']
i = 0
max_index = len(words) - 1

while i <= max_index:
    word = words[i]
    print(word + '!')
    i += 1

for word in words:
    print(word + '!')

for i in range(5):
    print('hello')


for i in range(0, 20, 2):
    print(i)
