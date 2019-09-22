class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class CircularLinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = Node(value)
        temp.next.next = self.head

    def print(self):
        if not self.head:
            return

        print(self.head.data, end='-')
        temp = self.head.next
        while temp != self.head:
            print(temp.data, end='-')
            temp = temp.next

    def prepend(self, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        
        self.head = Node(value)
        self.head.next = temp.next
        temp.next = self.head

    def remove(self, value):
        if not self.head:
            return
        elif self.head.data == value and self.head.next != self.head:
            temp3 = self.head
            # self.head = self.head.next
            # temp3 = None
            while temp3.next != self.head:
                temp3 = temp3.next

            temp4 = self.head
            self.head = self.head.next
            temp3.next = self.head
            temp4 = None
            return
        elif self.head.data == value and self.head.next == self.head:
            self.head = None
            return
        
        temp = self.head
        while temp.next != self.head:
            if temp.next.data == value:
                temp2 = temp.next
                temp.next = temp2.next
                temp2 = None
                return
            temp = temp.next

    def josephus(self, step):
        if not self.head or self.head.next == self.head:
            return None

        if step == 1:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            return temp.data
        elif step < 1:
            return 'Step size cannot be less than 1'

        temp = self.head
        while temp.next != temp:
            for _ in range(step-2):
                temp = temp.next
            temp2 = temp.next
            temp.next = temp2.next
            temp2 = None
            temp = temp.next
        return temp.data 

    def circular(self):
        if not self.head:
            return False

        temp = self.head
        while temp:
            if not temp.next:
                return False
            elif temp.next == self.head:
                return True
            temp = temp.next

lis = CircularLinkedList()
# lis.head = Node(1)
lis.append(2)
# lis.head.next = None
# lis.append(3)
# lis.head.next.next = Node(1)
# lis.append(4)
# # lis.print()
# lis.prepend(0)
# lis.print()
# lis.remove(2)
# lis.print()
# print(lis.josephus(200))
print(lis.circular())

def quad(a, b, c):
    return lambda x: a*x**2+b*x+c

print(quad(1,2,3))



