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
                print("Node is not present in left subtree")
            else:
                self.lchild.search(data)
        else:
            if self.rchild is None:
                print("Node is not present in the right subtree")
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
    def deleteNode(self, data):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild is not None:
                self.lchild = self.lchild.deleteNode(data)
            else:
                print("Given node is not present in th tree")
        elif data > self.key:
            if self.rchild is not None:
                self.rchild = self.rchild.deleteNode(data)
            else:
                print("Given node is not present in the tree")

        else:
            # if the node contains zero or one child
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None                           # inpection disabled : first argument of method is reassigned
                return temp
            # if the node contains two child node
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.deleteNode(node.key)
        return self




    def __str__(self):
        return f"{self.key}"


root = BST(10)
l = [23, 4, 67, 8, 1, 90, 2]

for data in l:
    root.insertNode(data)

root.deleteNode(2)
root.inorder()