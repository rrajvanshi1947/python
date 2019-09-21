class Node():
    def __init__(self, value=None):
        self.data = value
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = None

    def prepend(self, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = self.head

        temp = self.head
        while temp:
            temp = temp.next
            if temp.next == self.head:
                break
        self.head = Node(value)
        print(self.head.data)
        self.head.next = temp.next
        print(self.head.next.data)
        temp.next = self.head
        print(temp.next.data)

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = self.head

        temp = self.head
        while temp:
            temp = temp.next
            if temp.next == self.head:
                break
        temp.next = Node(value)
        temp.next.next = self.head

    def print(self):
        if not self.head:
            return
        
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
            if temp == self.head:
                return

lis = CircularLinkedList()
lis.head = Node(1)
lis.append(2)
lis.append(3)
lis.append(4)
# lis.prepend(0)
# print(lis.head.next.next.data)
lis.print()