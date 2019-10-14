class Node():
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def prepend(self, value):
        if not self.head:
            self.head = Node(value)
            return

        temp = self.head
        self.head = Node(value)
        self.head.next = temp
        temp.prev = self.head

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(value)
        temp.next.prev = temp

    def print(self):
        if not self.head:
            return

        temp = self.head
        while temp:
            print(temp.data, end = ' ')
            temp = temp.next

    def replace(self, key, value):
        if not self.head:
            self.append(value)
            return

        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if not temp:
            return 'Key not present'
        temp2 = temp
        temp = Node(value)
        temp.next = temp2.next
        temp.prev = temp2.prev
        if not temp2.prev:
            self.head = temp
        else:
            temp2.prev.next = temp
        if not temp2.next:
            pass
        else:
            temp2.next.prev = temp
            return
        temp2 = None

    def addAfter(self, key, value):
        if not self.head:
            self.head = Node(value)
            return

        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if not temp:
            return 'Value not present'
        temp2 = Node(value)
        temp2.next = temp.next
        if not temp2.next:
            pass
        else:
            temp2.next.prev = temp2
        temp2.prev = temp
        if not temp2.prev:
            self.head = temp2
        else:
            temp.next = temp2

    # def reverse(self):
    #     if not self.head or not self.head.next:
    #         return

    #     cur = self.head
    #     previous = temp = None
    #     while curr:
    #         temp = curr.prev
    #         curr.next = previous
    #         # curr.prev = temp
    #         previous.prev = curr
    #         temp.next = curr

    #         previous = curr
    #         curr = curr.prev

    def removeDuplicates(self):
        if not self.head or not self.head.next:
            return

        temp = self.head
        dic = {}
        while temp:
            if temp.data not in dic:
                dic[temp.data] = 1
                temp = temp.next
            else:
                temp.prev.next = temp.next
                if not temp.next:
                    break
                else:
                    temp.next.prev = temp.prev
                temp2 = temp
                temp = temp.next
                temp2 = None


def pairsWithSum(lis, sum):
    if not lis.head or not lis.head.next:
        return []

    arr = []
    dic = {}
    temp = lis.head
    while temp:
        if sum - temp.data not in dic:
            dic[temp.data] = 1
        else:
            arr.append((sum - temp.data, temp.data))
        temp = temp.next
    return arr
    

lis = DoublyLinkedList()
lis.append(1)
lis.append(1)
lis.append(4)
lis.append(3)
lis.prepend(21)
lis.append(5)
lis.append(3)
lis.append(1)
lis.append(0)
# lis.print()
# print(lis.replace(1,10))
lis.addAfter(5,2)
lis.removeDuplicates()
lis.print()
print(pairsWithSum(lis, 7))