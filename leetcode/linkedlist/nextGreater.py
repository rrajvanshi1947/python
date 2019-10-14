class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def nextLargerNodes(head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        
        if not head:
            return []
        
        temp, arr = head, []
        while temp:
            value = temp.val
            temp2 = temp.next
            while temp2:
                if temp2.val > value:
                    arr.append(temp2.val)
                    break
                temp2 = temp2.next
                if not temp2:
                    arr.append(0)
                
            temp = temp.next
            
        arr.append(0)
        return arr

first = Node(1)
first.next = Node(9)
first.next.next = Node(4)
# first.next.next.next = Node(11)
second = Node(1)
second.next = Node(5)
second.next.next = Node(4)

print(nextLargerNodes(first))
print(nextLargerNodes(second))

a= 'mississippi'
b = a.replace('ss','zz', 1)
print(b)