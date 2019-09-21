from linkedList import LinkedList

def merge(first, second):
    if not first.head or not second.head:
        return
    head1 = first.head
    head2 = second.head

    temp2 = head = None
    if head1.data <= head2.data:
        head = head1
        temp2 = head2
    else:
        head = head2
        temp2 = head1

    temp = head
    while temp.next:
        if temp.next.data > temp2.data:
            temp3 = temp.next
            temp.next = temp2
            temp4 = temp2.next
            temp2.next = temp3
            temp = temp2
            temp2 = temp4
            if not temp2:
                return
        else:
            temp = temp.next
            if not temp.next:
                temp.next = temp2
                return

linkedList = LinkedList()
linkedList.prepend(2)
# linkedList.printList()
linkedList.append(6)
# print(linkedList.head.data)
# linkedList.head.next = Node(6)
linkedList.append(8)
# linkedList.printList()
# linkedList.insertAfter(0,4)
# linkedList.printList()

linkedList2 = LinkedList()
linkedList2.prepend(3)
# linkedList.printList()
linkedList2.append(5)
# print(linkedList.head.data)
# linkedList.head.next = Node(6)
linkedList2.append(7)
linkedList2.append(9)
linkedList2.append(11)
linkedList2.append(13)

# linkedList.printList()
# linkedList.insertAfter(0,5)
# linkedList2.printList()

merge(linkedList, linkedList2)
linkedList.printList()
