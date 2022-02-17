class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head is None:
            print("Doubly Linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(f"{n.data}", end="-->")
                n = n.nref
            print("None")

    def print_LL_reverse(self):
        if self.head is None:
            print("Doubly Linked list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(f"{n.data}", end="-->")
                n = n.pref
            print("None")

    def insertInEmptyLinkedList(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linekd list is not empy")

    def addAtTheBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    def addAtTheEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref

            n.nref = new_node
            new_node.pref = n

    def addAfterNode(self, data, x):
        if self.head is None:
            print("Linked list is empty")

        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Node is not present in the linked list")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def addBeforeNode(self, data, x):
        if self.head is None:
            print("Linked list is empty")
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.nref
            if n is None:
                print("Node is not present in the linked list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

    def deleteAtTheBegin(self):
        if self.head is None:
            print("Linkked list is empty so we can not delete node from begining")
        else:
            n = self.head
            if n.nref is None:
                self.head = None
                print("DLL is empty after deleteing the node at the begining")
            else:
                n = self.head
                self.head = n.nref
                self.head.pref = None

    def deleteAtTheEnd(self):
        if self.head is None:
            print("Linkked list is empty so we can not delete node from end")
        else:
            n = self.head
            if n.nref is None:
                self.head = None
                print("DLL is empty after deleteing the node at the end")
            else:
                while n.nref is not None:
                    n = n.nref

                n.pref.nref = None

    def deleteByValue(self, x):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.nref is None:
            if self.head.data == x:
                self.head = None
            else:
                print(f"{x} is not present in the linked list")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref

        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print(f"{x} is not present in DLL")


db = DoublyLinkedList()
db.insertInEmptyLinkedList(23)
db.addAtTheEnd(234)
db.addAtTheBegin(45)
db.print_LL()
db.deleteByValue(234)
db.print_LL()
db.deleteByValue(45)
db.print_LL()
