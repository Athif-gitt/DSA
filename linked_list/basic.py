class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data

    def insert_at_end(self, data):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_data

    # def insert_at_pos(self, pos, data):

    

        


        
        



n1 = Node(1)
n2 = Node(2)

n1.next = n2


first = LinkedList(n1)

first.insert_at_beginning(12)
first.insert_at_end(24)

current = first.head
while current:
    print(current.data)
    current = current.next



