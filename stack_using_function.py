def create_stack():
    stack = []
    return stack


def check_empty(stack):
    return len(stack) == 0


def push(stack, items):
    stack.append(items)
    print("pushed item:", items)


def pop(stack):
    if check_empty(stack):
        return "stack is empty"
    return stack.pop()


stack = create_stack()
push(stack, 2)
push(stack, 4)
print(stack)
pop(stack)
print(stack)
