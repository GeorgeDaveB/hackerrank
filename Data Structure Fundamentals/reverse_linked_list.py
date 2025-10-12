# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def reverse(llist):
    if not llist:
        return None
    if not llist.next:
        return llist
    rev_tail = SinglyLinkedListNode(llist.data)  
    prev_rev = rev_tail
    while llist.next:
        llist = llist.next
        rev = SinglyLinkedListNode(llist.data)
        rev.next = prev_rev
        prev_rev = rev
    return rev

if __name__ == '__main__':
    llist = SinglyLinkedList()
    arr = [1,2,3,4,5]
    for x in arr:
        llist.insert_node(x)
    
    ### START : This is a commented block that was made without insert_node(self, node_data) 
    #
    # prev_node = SinglyLinkedListNode(arr[0])
    # llist.head = llist.tail = prev_node
    # for i in range (1,len(arr)):
    #     new_node = SinglyLinkedListNode(arr[i])
    #     prev_node.next = new_node
    #     prev_node = new_node
    # llist.tail = new_node # our last element. this will be the tail.
    #
    # END
    rev = reverse(llist.head)
    while rev:
        print(rev.data)
        rev = rev.next
    
    
        