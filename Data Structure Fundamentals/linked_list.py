class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
# class is defined.
# when we call the class and input a value like n = Node(10),
# then self remains as value 'self', and value takes as value the 10
# self basically is a variable that points to the generated object

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
    
    def get_node_at(self, index):
        if index < 0 or index > self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current 
    
