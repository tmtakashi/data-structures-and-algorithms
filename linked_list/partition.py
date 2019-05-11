class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def partition(node, x):
    head = node
    tail = node

    while != node None:
        nxt = node.next
        if node.value < x:


a = Node(3)
b = Node(5)
c = Node(8)
d = Node(5)
e = Node(10)
f = Node(2)
g = Node(1)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

head = partition(a, 5)

node = head
while node != None:
    print(node.value)
    node = node.next
