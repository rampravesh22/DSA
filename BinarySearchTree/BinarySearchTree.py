class BST:
    # for initialization of new node
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    # inserting the data in the tree
    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return

        if data < self.key:
            if self.lchild is None:
                self.lchild = BST(data)
            else:
                self.lchild.insert(data)
        elif data > self.key:
            if self.rchild is None:
                self.rchild = BST(data)
            else:
                self.rchild.insert(data)

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
        print(self.key,end=" ")
    def __str__(self):
        return f"{self.key}"


root = BST(10)
l = [23, 4, 67,8, 1, 90, 2]

for data in l:
    root.insert(data)
print("--------------------Preorder traversal---------------------------")
root.preorder()
print()
print("--------------------Inorder traversal---------------------------")
root.inorder()
print()
print("--------------------Postorder traversal---------------------------")
root.postorder()

