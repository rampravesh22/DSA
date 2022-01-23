class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dqueue(self):
        if len(self.queue) == 0:
            return None
        a=self.queue.pop(0)
        print(f"Deleted element is:a")

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(-23)
q.enqueue(45)
q.display()
q.dqueue()
q.dqueue()
print('After deletion:',end=" ")
print(q.display())
print(q.size())
