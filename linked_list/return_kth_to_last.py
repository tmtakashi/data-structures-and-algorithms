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
    right_pointer = head
    left_pointer = head

    # Move the right pointer (k-1)steps ahead
    for _ in range(k - 1):
        right_pointer = right_pointer.next

    while right_pointer.next != None:
        right_pointer = right_pointer.next
        left_pointer = left_pointer.next

    return left_pointer


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

print(kth_to_last(a, 2).value)
