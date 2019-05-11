class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


def delete_middle_node(head):
    faster = head
    slower = head

    while faster.next and faster.next.next:
        faster = faster.next.next
        slower = slower.next

    current = head
    prev = head
    while current != None:
        if current == slower:
            prev.next = current.next
        else:
            prev = current
        current = current.next


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

delete_middle_node(a)

while a != None:
    print(a.value)
    a = a.next
