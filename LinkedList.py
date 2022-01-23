class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data}", end="-->")
                n = n.ref

            print('None')

    def addAtBegin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def addAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def addAfterNode(self, data, x):  # x is after which node we are inseting the data
        n = self.head
        while n is not None:
            if n.data == x:
                break
            else:
                n = n.ref
        if n is None:
            print(f"The node with data: {x} is not present in the linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def addBeforeNode(self, data, x):
        new_node = Node(data)
        n = self.head
        if n is None:
            print("Linked list is empty")
            return
        if n.data == x:
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node.ref = n.ref
            n.ref = new_node

    def addElementToEmpty(self, data):
        new_node = Node(data)
        if self.head is not None:
            print("Linked list is not empty")
        else:
            self.head = new_node

    def deleltFirstNode(self):
        if self.head is None:
            print("linked list is empty so we can not delete the first node")
        else:
            self.head = self.head.ref

    def deleteLastNode(self):
        n = self.head


l = LinkedList()
l.addAtBegin(10)
l.addAtBegin(20)
l.addAtBegin(30)
l.deleteLastNode()
l.print_ll()
