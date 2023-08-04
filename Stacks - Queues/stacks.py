class Stack:
    def __init__(self):
        self.items = []  # Constructor: initialize an empty list for the stack

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def push(self, item):
        # Push an item onto the stack
        self.items = self.items + [item]

    def pop(self):
        # Pop an item from the stack
        if not self.is_empty():
            item = self.items[-1]
            self.items = self.items[:-1]
            return item

    def top(self):
        # Return the top element of the stack without removing it
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        # Return the size of the stack
        count = 0
        for _ in self.items:
            count += 1
        return count


# Test
stack = Stack()

stack.push("emrah")
print("Top element:", stack.top())

stack.push(15)
print("Top element:", stack.top())

print("\nSize:", stack.size())

stack.pop()
print("Top element after pop:", stack.top())
