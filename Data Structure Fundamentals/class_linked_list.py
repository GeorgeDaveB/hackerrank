class Node:
    """A single node in a singly linked list."""
    def __init__(self, value):
        self.value = value      # The data stored in this node
        self.next = None        # Pointer to the next node


class LinkedList:
    """A standard singly linked list."""
    def __init__(self):
        self.head = None        # First node
        self.tail = None        # Last node (for fast appends)
        self.length = 0         # Keep track of number of elements

    def append(self, value):
        """Add a node to the end of the list."""
        new_node = Node(value)
        if not self.head:
            # Empty list → head and tail are the same
            self.head = self.tail = new_node
        else:
            # Attach to the end
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Add a node to the beginning of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get_node_at(self, index):
        """Return the node at a specific index."""
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def insert(self, index, value):
        """Insert a node before the node at the given index."""
        if index <= 0:
            return self.prepend(value)
        if index >= self.length:
            return self.append(value)

        new_node = Node(value)
        prev = self.get_node_at(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1

    def remove(self, index):
        """Remove a node at a specific index."""
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            removed = self.head
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            prev = self.get_node_at(index - 1)
            removed = prev.next
            prev.next = removed.next
            if index == self.length - 1:
                self.tail = prev
        self.length -= 1
        return removed.value

    def __len__(self):
        """Return the number of nodes in the list."""
        return self.length

    def __iter__(self):
        """Allow iteration through the list (e.g., for value in linked_list)."""
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        """Return a readable string representation of the list."""
        values = [str(v) for v in self]
        return " -> ".join(values) if values else "Empty List"
