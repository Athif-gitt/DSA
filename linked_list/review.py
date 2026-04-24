class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, head):
        self.head = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            return
        current.next = new_node
        
    def insert_at_middle(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        
    def del_at_beginning(self):
        first = self.head
        second = self.head.next
        first.next = None
        self.head = second
    
    def delete_at_end(self):
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        
            
            
        
        
        
        
        
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3

first = LinkedList(n1)
first.insert_at_beginning(0)
first.insert_at_end(4)
first.del_at_beginning()
first.insert_at_middle(5, 1)
# first.delete_at_end()

current = first.head
while current:
    print(current.data, end='->')
    current = current.next
print("None")
    

        