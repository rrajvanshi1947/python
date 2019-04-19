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
        if self.head is None:
            self.head = new_node
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
            return 'List is empty'
        elif self.head.data == value:
            node = self.head
            self.head = self.head.next
            node = None
        else:
            curr_node = self.head
            while curr_node.data != value:
                curr_node = curr_node.next

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


testNode = Node(3)
print(testNode.data, testNode.next)

testLinkedList = LinkedList()
testLinkedList.deleteNode(4)
testLinkedList.append(1)
testLinkedList.append(2)
testLinkedList.append(3)
testLinkedList.append(4)
testLinkedList.prepend(0)
testLinkedList.insert_after_node(7, .5) 
testLinkedList.insert_after_node(2, .5)
testLinkedList.printList()
print(testLinkedList.length())
print(testLinkedList.len_recursive(testLinkedList.head))


# text = '51d0079174baa712fd60c9c4a3f926dfc443e045423eb2b5a298589d56a3ff97'
# print(len(text))