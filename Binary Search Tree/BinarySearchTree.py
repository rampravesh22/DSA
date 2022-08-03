class BST:
    # for initialization of new node
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    # inserting the data in the tree
    def insertNode(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return

        if data < self.key:
            if self.lchild is None:
                self.lchild = BST(data)
            else:
                self.lchild.insertNode(data)
        elif data > self.key:
            if self.rchild is None:
                self.rchild = BST(data)
            else:
                self.rchild.insertNode(data)

    # Searching data/node present in the tree or not
    def search(self, data):
        if self.key == data:
            print("Node is found at")
            return
        if data < self.key:
            if self.lchild is None:
                print("\nNode is not present in left subtree")
            else:
                self.lchild.search(data)
        else:
            if self.rchild is None:
                print("\nNode is not present in the right subtree")
            else:
                self.rchild.search(data)

    # Traversal operation in tree
    # 1- Pre order traversal
    def preorder(self):
        print(self.key, end=" ")
        if self.lchild is not None:
            node = self.lchild
            node.preorder()
        if self.rchild is not None:
            node = self.rchild
            node.preorder()

    # 2- In order traversal
    def inorder(self):
        if self.lchild is not None:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild is not None:
            self.rchild.inorder()

    # 3- Post order traversal
    def postorder(self):
        if self.lchild is not None:
            self.lchild.postorder()
        if self.rchild is not None:
            self.rchild.postorder()
        print(self.key, end=" ")

    # Deletion operation
    def deleteNode(self, data, curr):
        if self.key is None:
            print("\nTree is empty")
            return
        if data < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.deleteNode(data, curr)
            else:
                print("\nGiven node is not present in the tree")
        elif data > self.key:
            if self.rchild is not None:
                self.rchild = self.rchild.deleteNode(data, curr)
            else:
                print("\nGiven node is not present in the tree")

        else:
            # if the node contains zero or one child
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None  # inpection disabled : first argument of method is reassigned
                return temp
            # if the node contains two child node
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.deleteNode(node.key)
        return self

    # Find node with the smallest key
    def minNode(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("Node with smallest key is ", current.key, sep=": ")

    # Find node with the smallest key
    def maxNode(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Node with biggest key is ", current.key, sep=": ")

    # This is for printing the root node
    def __str__(self):
        return f"{self.key}"


# this function is to count numbers of node in the BST
def countNode(node):
    if node is None:
        return 0
    else:
        return 1 + countNode(node.lchild) + countNode(node.rchild)


root = BST(100)
for node in [12, 3, 4, 89, 14, 34]:
    root.insertNode(node)
if countNode(root) > 1:  # I don't want to delete if the tree contains only one node so, I will print the else condition
    pass
    # root.deleteNode(1, root.key)
else:
    print("Can't perform this operation")
root.preorder()
print()
root.minNode()
root.maxNode()
