class Node():
    def __init__(self, value=None):
        self.data = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:    
            self.head = Node(value)
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(value)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end= '-')
            temp = temp.next

    def prepend(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertAfter(self, nodeIndex, value):
        if not self.head:
            return

        temp = self.head
        for i in range(nodeIndex):
            temp = temp.next
        temp2 = temp.next
        temp.next = Node(value)
        temp.next.next = temp2

    def deleteNode(self, value):
        if not self.head:
            return
        elif self.head.data == value:
            temp = self.head
            self.head = temp.next   
            temp = None         
            return

        temp = self.head
        while temp:
            if not temp.next:
                return
            if temp.next.data == value:
                temp2 = temp.next
                temp.next = temp2.next
                temp2 = None
            temp = temp.next

    def deletePosition(self, pos):
        if not self.head:
            return
        elif pos == 0:
            temp = self.head
            self.head = temp.next
            temp = None
            return

        temp = self.head
        for i in range(pos-1):
            temp = temp.next
            if not temp.next:
                return
        temp2 = temp.next
        temp.next = temp2.next
        temp2 = None 

    def length(self):
        if not self.head:
            return 0
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length

    def lengthRecursive(self, node):
        if not node:
            return 0
        
        return 1 + self.lengthRecursive(node.next)

    def swapNodes(self, key1, key2):
        if not self.head:
            return 

        temp = self.head
        temp2 = None
        while temp:
            if temp.next.data == key1:
                temp2 = temp.next
                break
            temp = temp.next
        if not temp2:
            return 'Key1 missing'
        temp5 = temp2.next

        temp3 = self.head
        temp4 = None
        while temp3:
            if temp3.next.data == key2:
                temp4 = temp3.next
                break
            temp3 = temp3.next
        if not temp4:
            return 'Key2 missing'
        temp6 = temp4.next

        temp2.next = temp6
        temp4.next = temp5
        temp.next = temp4
        temp3.next = temp2

        
        


        



first = Node(5)
second = first.next = Node(7)
third = second.next = Node(9)
fourth = third.next = Node(11)

linkedList = LinkedList()
linkedList.prepend(2)
# linkedList.printList()
linkedList.append(4)
# print(linkedList.head.data)
# linkedList.head.next = Node(6)
linkedList.append(8)
# linkedList.printList()
linkedList.insertAfter(0,1)
# linkedList.printList()
linkedList.deleteNode(90)
# linkedList.printList()
linkedList.deletePosition(1)
linkedList.printList()
print(linkedList.length())
print(linkedList.lengthRecursive(linkedList.head))