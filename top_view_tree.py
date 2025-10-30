class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def goLeft(root, width, comparer):
    if root == None:
        return
    if width < comparer:      
        print(root.info, end=" ")
        comparer = width
    goLeft(root.left, width - 1, comparer)
    goLeft(root.right, width + 1, comparer)

def goRight(root, width, comparer):
    if root == None:
        return
    if width < 0:
        if width < comparer:
            print(root.info, end=" ")
            comparer = width
    goRight(root.right, width + 1, comparer)
    goRight(root.left, width - 1, comparer)




    
def topView(root):
    width = 0
    comparer = 0
    goRight(root.left, width -1 , comparer)
    print(root.info, end=" ")
    goLeft(root.right, width +1,comparer)



tree = BinarySearchTree()
t = 15

arr = [1, 14, 3, 7, 4, 5, 15, 6, 13, 10, 11, 2, 12, 8, 9]

for i in range(t):
    tree.create(arr[i])

topView(tree.root) 
#expected output:     2 1 14 15 12 