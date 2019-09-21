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

    # def swapNodes(self, key1, key2):
    #     if not self.head:
    #         return 

    #     temp = self.head
    #     temp2 = None
    #     while temp:
    #         if temp.next.data == key1:
    #             temp2 = temp.next
    #             break
    #         temp = temp.next
    #     if not temp2:
    #         return 'Key1 missing'
    #     temp5 = temp2.next

    #     temp3 = self.head
    #     temp4 = None
    #     while temp3:
    #         if temp3.next.data == key2:
    #             temp4 = temp3.next
    #             break
    #         temp3 = temp3.next
    #     if not temp4:
    #         return 'Key2 missing'
    #     temp6 = temp4.next

    #     temp2.next = temp6
    #     temp4.next = temp5
    #     temp.next = temp4
    #     temp3.next = temp2

    def swapNodes(self, x, y): 
  
        # Nothing to do if x and y are same 
        if x == y: 
            return 
  
        # Search for x (keep track of prevX and CurrX) 
        prevX = None
        currX = self.head 
        while currX != None and currX.data != x: 
            prevX = currX 
            currX = currX.next
  
        # Search for y (keep track of prevY and currY) 
        prevY = None
        currY = self.head 
        while currY != None and currY.data != y: 
            prevY = currY 
            currY = currY.next
  
        # If either x or y is not present, nothing to do 
        if currX == None or currY == None: 
            return 
        # If x is not head of linked list 
        if prevX != None: 
            prevX.next = currY 
        else: #make y the new head 
            self.head = currY 
  
        # If y is not head of linked list 
        if prevY != None: 
            prevY.next = currX 
        else: # make x the new head 
            self.head = currX 
  
        # Swap next pointers 
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def reverse(self):
        if not self.head:
            return
        elif not self.head.next:
            return
        
        prev = temp = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        
    def reverseRecursive(self, node):
        if not self.node:
            return
        elif not self.node.next:
            return

        def recurs(self, node, prev):
            if not node:
                return prev
            temp = node.next
            node.next = prev
            prev = node
            node = temp    
            self.recurs(node, prev)
        
        self.head = self.recurs(self.head, prev=None)

    def removeDuplicates(self):
        if not self.head or not self.head.next:
            return

        temp = self.head
        dic = {}
        dic[temp.data] = 1
        while temp.next:
            if temp.next.data in dic:
                temp2 = temp.next
                temp.next = temp2.next
                temp2 = None
                continue
            dic[temp.next.data] = 1
            temp = temp.next
            
    def rotate(self, pos):
        if not self.head or not self.head.next:
            return
    
        temp = self.head
        for i in range(pos):
            temp = temp.next
            if not temp:
                return 'Position out of range'

        if not temp.next:
            return
        temp2 = self.head
        self.head = temp.next
        temp.next = None

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = temp2

    def palindrome(self):
        if not self.head:
            return False
        elif not self.head.next:
            return True

        temp = self.head
        arr = []
        while temp:
            arr.append(temp.data)
            temp = temp.next

        if len(arr)%2 == 0:
            quotient = int(len(arr)/2)
            arr2 = arr[quotient:]
            if arr[:quotient] == arr2[::-1]:
                return True
            else:
                return False
        else:
             quotient = int(len(arr)//2)
             arr2 = arr[quotient+1:]
             if arr[:quotient] == arr2[::-1]:
                return True
             else:
                return False

    def moveTail(self):
        if not self.head or not self.head.next:
            return

        temp = temp2 = self.head
        while temp.next.next:
            temp = temp.next
        self.head = temp.next
        temp.next = None
        self.head.next = temp2

    


        

        
def sumLists(first, second):
    if not first.head and not second.head:
        return

    number1 = number2 = ''
    temp = first.head
    while temp:
        number1 += str(temp.data)
        temp = temp.next

    temp = second.head
    while temp:
        number2 += str(temp.data)
        temp = temp.next
    
    if number1 == '':
        number1 = 0
    elif number2 == '':
        number2 = 0

    # for num in [number1, number2]:
    #     if num == '':
    #         num = 0
    print(number2, number1)
    return int(number1) + int(number2)


first = Node(5)
second = first.next = Node(7)
third = second.next = Node(9)
fourth = third.next = Node(11)

linkedList = LinkedList()
linkedList2 = LinkedList()
# linkedList.prepend(2)
# linkedList.printList()
linkedList.append(2)
# print(linkedList.head.data)
# linkedList.head.next = Node(6)
linkedList.append(6)
linkedList.append(8)
# linkedList2.append(8)

# linkedList2.append(6)

# linkedList2.append(4)

# linkedList.append(1)

# linkedList.append(2)

# # linkedList.printList()
# linkedList.insertAfter(0,1)
# linkedList.printList()
linkedList.deleteNode(90)
# linkedList.printList()
# linkedList.deletePosition(1)
# linkedList.printList()
# print(linkedList.length())
# print(linkedList.lengthRecursive(linkedList.head))
# linkedList.reverse()
# linkedList.removeDuplicates()
# linkedList.rotate(4)
# linkedList.moveTail()
linkedList.printList()
# print(linkedList.palindrome())
print(sumLists(linkedList, linkedList2))