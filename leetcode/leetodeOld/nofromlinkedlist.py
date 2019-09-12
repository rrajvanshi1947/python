class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


def addTwoNumbers(l1, l2):
    string1 = ''
    string2 = ''
    arr1 = []
    temp = l1
    # arr2 = []
    while temp:
        arr1.append(temp.val)
        temp = temp.next
    temp = l2
    while temp:
        arr1.append(temp.val)
        temp = temp.next
    for i in range(2,-1,-1):
        string1 += str(arr1[i])
    for i in range(5,2,-1):
        string2 += str(arr1[i])    
    number = int(string1) + int(string2)
    string3 = str(number)
    l3 = Node(int(string3[0]))
    l4 = Node(int(string3[1]))
    l5 = Node(int(string3[2]))
    l3.next = l4
    l4.next = l5
    print(l3.val,l4.val,l5.val)

l1 = Node(1)
l2 = Node(2)
l3 = Node(3)
l1.next = l2
l2.next = l3

l4 = Node(4)
l5 = Node(5)
l6 = Node(6)
l4.next = l5
l5.next = l6

print(addTwoNumbers(l1, l4))