# Node class to represent individual elements in the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Append data to the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            self.tail = new_node

    # Display the elements of the list in forward direction
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Display the elements of the list in reverse direction
    def display_reverse(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.append("ankara")
dll.append("bolu")
dll.append("izmir")

# Display the original Doubly Linked List
print("Doubly Linked List:")
dll.display()

# Display the reversed Doubly Linked List
print("\nReversed Doubly Linked List:")
dll.display_reverse()
