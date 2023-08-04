class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)  # Enqueue by adding the item to the end of the list.

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.items[0]  # Get the first item (FIFO behavior)
            self.items = self.items[1:]  # Remove the first item from the list
            return removed_item
        else:
            raise IndexError("dequeue from empty queue")

    def size(self):
        return len(self.items)

# Test
queue = Queue()

queue.enqueue("yağmur")
queue.enqueue(16)
print("Size: ", queue.size())  # Output: Size: 2

queue.dequeue()
print("Size: ", queue.size())  # Output: Size: 1
