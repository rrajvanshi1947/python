class Node():
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def partition(head, x):
    if not head or not head.next:
        return head
    
    temp = head
    temp2 = temp3 = None
    while temp.next:
        if temp.next.val >= x:
            if not temp2:
                temp2 = temp.next
                temp.next = temp2.next
                # continue
            else:
                if not temp3:
                    temp3 = temp.next
                    temp.next = temp3.next
                    temp2.next = temp3
                else:
                    temp3.next = temp.next
                    temp.next = temp3.next
                    temp3 = temp3.next
        else:
            temp = temp.next
            
    temp.next = temp2
    if temp3:
        temp3.next = None
    else:
        temp2.next = None
    return head

def printList(head):
        temp = head
        while temp:
            print(temp.data, end= '-')
            temp = temp.next


first = Node(1)
second = first.next = Node(4)
third = second.next = Node(3)
# fourth = third.next = Node(2)
# fifth = fourth.next = Node(5)
# sixth = fifth.next = Node(2)

n = partition(first, 3)
printList(n)