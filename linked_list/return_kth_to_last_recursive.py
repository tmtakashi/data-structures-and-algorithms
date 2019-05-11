class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def append_to_tail(self, value):
        end = Node(value)
        n = self
        while n.next != None:
            n = n.next
        n.next = end


def kth_to_last(head, k):
    if head == None:
        return 0
    index = kth_to_last(head.next, k) + 1
    if index == k:
        print(k, 'th to the last node is ', head.value)
    return index


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

kth_to_last(a, 2)
