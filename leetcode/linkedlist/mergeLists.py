class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1, l2):
    if not l1 and not l2:
        return None
    elif l1 and not l2:
        return l1
    elif l2 and not l1:
        return l2
    
    head = temp1 = temp2 = None
    if l1.val <= l2.val:
        head = l1
        temp1 = l1.next
        temp2 = l2
    else:
        head = l2
        temp2 = l2.next
        temp1 = l1

    print(head.val)
    
    temp = head.next
    # temp1, temp2 = l1, l2
    while temp1 and temp2:
        if temp1.val <= temp2.val:
            temp = temp1
            temp1 = temp1.next
        else:
            temp = temp2
            temp2 = temp2.next

        print(temp.val)    
        temp = temp.next
        
    if temp1:
        temp = temp1
    if temp2:
        temp = temp2
        
    while temp:
        print(temp.val)
        temp = temp.next

    return head

first = Node(1)
first.next = Node(2)
first.next.next = Node(4)
# first.next.next.next = Node(11)
second = Node(1)
second.next = Node(3)
second.next.next = Node(4)

mergeTwoLists(first, second)

a = 1
b = False
c =  True or a
print(c)