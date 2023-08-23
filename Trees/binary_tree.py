class Node:
    def __init__(self, key):
        self.value = key 
        
        self.right = None
        self.left = None
        
# create root 
root = Node("A")
root.left = Node("B")
root.left.left = Node("D")
root.right = Node("C")

