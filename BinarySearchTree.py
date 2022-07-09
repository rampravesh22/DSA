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
            if self.lchild is not None:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        elif data > self.key:
            if self.rchild is not None:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    # Searching data/node present in the tree or not
    def search(self, data):
        if self.key == data:
            print("Node is found at")
            return
        if data < self.key:
            if self.lchild is not None:
                self.lchild.search(data)
            else:
                print("Node is not present in left subtree")
        else:
            if self.rchild is not None:
                self.rchild.search(data)
            else:
                print("Node is not present in the right subtree")

    # Traversal operation in tree
    # 1- Pre order traversal
    # 2- In order traversal
    # 3- Post order traversal

    def __str__(self):
        return f"{self.key}"


root = BST(10)
l = [23, 4, 67, 1, 90, 2]

for data in l:
    root.insert(data)

root.search(60)
