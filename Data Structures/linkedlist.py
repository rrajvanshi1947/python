class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self): 
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def insert_after_node(self, prev_node, data):
        # if not prev_node:
        #     print('Given node doesn\'t exist')
        new_node = Node(data)
        # new_node.next = prev_node.next
        # prev_node.next = new_node
        curr_node = self.head
        for i in range(1, prev_node):
            curr_node = curr_node.next
            if curr_node.next == None:
                print('Node out of context')
                return

        new_node.next = curr_node.next
        curr_node.next = new_node

    def deleteNode(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            temp = self.head
            self.head = self.head.next
            temp = None
        curr_node = self.head
        prev = None
        while curr_node:
            prev = curr_node
            if curr_node.data == value:
                break
            curr_node = curr_node.next
        if curr_node is None:
            return
        else:
            prev = curr_node.next
            curr_node = None

    def deleteNodePosition(self, position):
        if self.head is None:
            return
        if position == 1:
            temp = self.head
            self.head = self.head.next
            temp = None
        curr_node = self.head
        for i in range(1, position - 1):
            curr_node = curr_node.next
            if curr_node is None:
                break
        if curr_node is None:
            return
        temp = curr_node.next
        curr_node.next = curr_node.next.next
        temp = None

    def length(self):
        curr_node = self.head
        counter = 0
        while curr_node is not None:
            counter += 1
            curr_node = curr_node.next
        return counter

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swapNode(self, value1, value2):
        if value1 == value2:
            return
        curr_node = self.head
        # prev1 = prev2 = None
        while curr_node:
            # print(curr_node.data)
            # prev1 = curr_node
            if curr_node.data == value1 or curr_node.data == value2:
                break
            curr_node = curr_node.next
        new_curr_node = curr_node
        if curr_node.data == value1:
            while new_curr_node and new_curr_node.data != value2:
                new_curr_node = new_curr_node.next
            curr_node.data, new_curr_node.data = new_curr_node.data, curr_node.data
        else:
            while new_curr_node and new_curr_node.data != value1:
                new_curr_node = new_curr_node.next
            curr_node.data, new_curr_node.data = new_curr_node.data, curr_node.data

         
        



testNode = Node(3)
print(testNode.data, testNode.next)

testLinkedList = LinkedList()
testLinkedList.deleteNode(4)
testLinkedList.deleteNodePosition(3)
testLinkedList.append(1)
testLinkedList.append(2)
testLinkedList.append(3)
testLinkedList.append(4)
testLinkedList.append(6)
testLinkedList.append(8)
testLinkedList.prepend(0)
testLinkedList.insert_after_node(7, .5) 
testLinkedList.insert_after_node(2, .5)
# testLinkedList.printList()
testLinkedList.deleteNodePosition(3)
# testLinkedList.printList()
testLinkedList.swapNode(0,1)
testLinkedList.printList()
print(testLinkedList.length())
print(testLinkedList.len_recursive(testLinkedList.head))