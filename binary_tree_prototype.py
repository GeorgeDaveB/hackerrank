class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root= None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left:
                self._insert(node.left, key)
            else:
                node.left = Node(key)
        elif key > node.key:
            if node.right:
                self._insert(node.right, key)
            else:
                node.right = Node(key)
        else:
            pass # equal keys are not inserted in this version