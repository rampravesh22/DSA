class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

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

    def __str__(self):
        return f"{self.key}"


root = BST(None)
l = [23, 4, 67, 1, 90, 2]
for item in l:
    root.insert(item)

print(root)
