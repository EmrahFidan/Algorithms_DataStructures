# Stack using the list

stack = ["emrah",4,7,"learning"]
stack.append("deep")
stack.append("machine") # append = push 


print(stack) 

print(stack.pop()) 

print(stack) 


#?  making Queue using list and deque

from collections import deque

queue = deque(["emrah",4,7,"learning"])

print(queue)

queue.insert(0,"deep")
print(queue)

queue.insert(0,"machine")
print(queue)

queue.pop()
print(queue)


