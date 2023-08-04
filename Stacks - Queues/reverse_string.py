def create_stack():
    return []

def stack_size(stack):
    return len(stack)

def top(stack):
    if not is_empty(stack):
        return stack[-1]
    raise IndexError("Stack is empty.")

def is_empty(stack):
    return len(stack) == 0

def push(stack, value):
    stack.append(value)

def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    raise IndexError("Stack is empty.")

def reverse_string(string):
    n = len(string)
    stack = create_stack()

    for char in string:
        push(stack, char)

    new_string = ""

    for i in range(n):
        new_string += pop(stack)

    return new_string

# Test
print("Machine Learning => ", reverse_string("Machine Learning"))
