str = "Hello World"
stack = []
for char in str:
    stack.append(char)

rev = ""

while stack:
    rev += stack.pop()

print(rev)
