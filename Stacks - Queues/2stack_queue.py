class Queue2Stack:
    def __init__(self):
        # Initialize 2 stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        # Add an element to the queue
        self.stack1.append(element)

    def dequeue(self):
        # stack1 send push into pop leaf satck2
        # stack1 = [1,2,3] # stack2.append(stack1.pop())
        # stack2 = [3,2,1] # queue.pop() = 1
        # queue = [3,2,1]  # queue.pop() = 1
    
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        # Pop the element from stack2, which was added first to stack1
        # and is therefore the oldest element in the queue
        if self.stack2:
            return self.stack2.pop()
        else:
            raise IndexError("Queue is empty.")

# Test
queue = Queue2Stack()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3




