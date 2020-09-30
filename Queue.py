class Queue:
    def __init__(self):
        self.items=[]
    def is_emppty(self):
        return self.items ==[]
    def enqueue(self,item):
        self.items.insert(0, item)
    def dequeue(self):
        self.items.pop()
    def size(self):
        return len(self.items)
    def value(self):
        return self.items

a_queue=Queue()
for i in range(1,8):
    a_queue.enqueue(i)
a_queue.dequeue()
print(str(a_queue.value()))