class Node:
    def __init__(self, value):
        """Creates a new Node with the given value."""
        self.value = value
        self.next_node = None
        
    def set_next_node(self, node):
        """Sets the next Node in the sequence."""
        self.next_node = node
        
    def get_next_node(self):
        """Returns the next Node in the sequence."""
        return self.next_node
    
    def get_node_value(self):
        """Returns the value stored in the Node."""
        return self.value

# Creating nodes for cities with their corresponding license plate codes
ankara = Node("06")
bolu = Node("14")
izmir = Node("35")

# Linking nodes together: ankara => bolu => izmir
ankara.set_next_node(bolu)  # Ankara is followed by Bolu
bolu.set_next_node(izmir)   # Bolu is followed by Izmir

# Displaying the linked node values
print(ankara.get_next_node().get_node_value())  # Should print "14" (Bolu's code)
print(bolu.get_next_node().get_node_value())    # Should print "35" (Izmir's code)
