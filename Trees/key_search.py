class Node:
    def __init__(self, key):
        self.value = key
        
        self.right = None
        self.left = None
        
def search(root,key):
    # base case 
    if root is None or root.value == key: # aradığım root'a veya root yoksa
        return root
    
    if root.value < key:
        return search(root.right,key)
    else:
        return search(root.left,key)
    
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.value < node.value:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
    
tree = Node(41)

insert(tree, Node(65))
insert(tree, Node(99))
insert(tree, Node(50))
insert(tree, Node(20))
insert(tree, Node(11))
insert(tree, Node(29))

print(search(tree,50).value)