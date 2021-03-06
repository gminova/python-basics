import re

pattern = r'spam'

if re.match(pattern, 'spamspamspam'):
    print('Match')
else:
    print('No match')

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

# re.sub(pattern, repl, string, count=0)
str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str, 1)
print(newstr)
