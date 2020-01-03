import re
pattern = r'gr.y'

if re.match(pattern, 'grey'):
    print('Mahched grey')
if re.match(pattern, 'gray'):
    print('Mahched gray')
if re.match(pattern, 'blue'):
    print('Mahched blue')

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")
