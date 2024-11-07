def push(stack, item):
    stack.append(item)
def pop(stack):
    return stack.pop()
str = 'nathan'
print(str)
n = len(str)
stack = []
for i in range(0, n, 1):
    push(stack ,str[i])
str = ''
for i in range(0, n, 1):
    str += pop(stack)
print(str)

    