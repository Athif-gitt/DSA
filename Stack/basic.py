# stack = []
# if not stack:
#     print("stack is empty")
# else:
#     print("stack occupied")

# stack = [10, 20, 30] # Stack with elements
# top_element = stack.pop() # Popping the topmost element
# print("Popped element:", top_element)

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def is_empty(self):
#         return len(self.stack) == 0
    
#     def push(self, value):
#         self.stack.append(value)
    
#     def top(self):
#         if stack.is_empty():
#             return("Empty Stack")
        
#         return self.stack[-1]
    
#     def size(self):
#         return len(self.stack)

# stack = Stack()
# stack.push(1)
# print(stack.is_empty())
# print(stack.top())
# print(stack.size())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def display(self):
        current = self.top
        while current:
            print(current.data, end='->')
            current = current.next
        print("None")

s = Stack()

s.push(1)
s.display()
    

        
