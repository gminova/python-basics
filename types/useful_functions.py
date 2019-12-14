print(", ".join(["spam", "eggs", "ham"]))

print("Hello ME".replace("ME", "world"))

print("This is a sentence.".startswith("This"))

print("This is a sentence.".endswith("sentence."))

print("This is a sentence.".upper())

print("AN ALL CAPS SENTENCE".lower())

print("spam, eggs, ham".split(", "))


print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)
