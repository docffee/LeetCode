class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None                    # Head is front of list

    def append(self, data):
        if not self.head:                   # Add node if no other nodes
            self.head = Node(data)          # Assign head to new node
            self.head.next = self.head      # Point to self if only node
        else:
            new_node = Node(data)           # If other nodes exist
            cur = self.head                 # Start count from head node
            while cur.next != self.head:    # Iterate until last node
                cur = cur.next              # Last node points to self.head
            cur.next = new_node             # Add new node
            new_node.next = self.head       # Point new node to head

    def preprend(self, data):
        new_node = Node(data)               # Add new node to front
        cur = self.head                     # Save self.head position as cur
        new_node.next = self.head           # Point new node to head

        if not self.head:
            new_node.next = new_node        # Point to self if no other nodes
        else:
            while cur.next != self.head:    # Find last node from front
                cur = cur.next              # Iterate counter to last node
            cur.next = new_node             # Point last node to new node
        self.head = new_node                # Assign new node as head

    def print_list(self):
        cur = self.head                     # Start from head of list

        while cur:                          # While not null
            print(cur.data)                 # Print data
            cur = cur.next                  # Iterate
            if cur == self.head:            # If returned to head break
                break


c = CircularLinkedList()
c.append('C')
c.append('D')
c.preprend('B')
c.preprend('A')
c.print_list()
