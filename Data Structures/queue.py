class Queue:
    def __init__(self):
        self.queue = []

    def put(self, value):
        self.queue.append(value)

    def extract(self):
        if self.queue:
            print(self.queue[0])
            self.queue = self.queue[1:]
        #self.queue.pop(0)

    def empty(self):
        return self.queue == []

    def printQ(self):
        print(self.queue)

q = Queue()
for i in range(5):
    q.put(i)
q.printQ()
q.extract()
print(q.empty())
q.printQ()
for i in range(4):
    q.extract()
print(q.empty())
