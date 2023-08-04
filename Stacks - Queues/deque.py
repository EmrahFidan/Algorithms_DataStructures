class MyDeque:
    def __init__(self):
        self.items = []  # Initialize the deque with an empty list.

    def is_empty(self):
        return not self.items  # Return True if the deque is empty, False otherwise.

    def add_front(self, item):
        self.items.append(item)  # Add the 'item' to the front of the deque (end of the list).

    def add_rear(self, item):
        self.items.insert(0, item)  # Add the 'item' to the rear of the deque (beginning of the list).

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)  # Remove and return the front (first) item from the deque.
        raise IndexError("Deque is empty. Cannot remove from the front.")

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()  # Remove and return the rear (last) item from the deque.
        raise IndexError("Deque is empty. Cannot remove from the rear.")

    def size(self):
        return len(self.items)  # Return the current size (number of elements) of the deque.


# Test
deque = MyDeque()  # Create a new instance of MyDeque.

deque.add_front("deep")  # Add "deep" to the front of the deque. The deque now contains ['deep'].
deque.add_rear("learning")  # Add "learning" to the rear of the deque. The deque now contains ['learning', 'deep'].
deque.add_rear(8)  # Add 8 to the rear of the deque. The deque now contains [8, 'learning', 'deep'].

print("Size:", deque.size())  # Print the size of the deque, which is 3.

deque.remove_front()  # Remove and return the front item from the deque ('deep'). The deque now contains [8, 'learning'].
deque.remove_rear()  # Remove and return the rear item from the deque (8). The deque now contains ['learning'].

print("Size:", deque.size())  # Print the size of the deque, which is 1.
