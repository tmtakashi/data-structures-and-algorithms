class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def intersection(head1, head2):
    length1 = 0
    length2 = 0

    n1 = head1
    n2 = head2

    while n1.next != None:
        length1 += 1
        n1 = n1.next

    while n2.next != None:
        length2 += 1
        n2 = n2.next

    intersect = True if n1 is n2 else False

    n1 = head1
    n2 = head2

    if intersect:
        if length1 < length2:
            diff = length2 - length1
            for _ in range(diff):
                n2 = n2.next
        elif length1 > length2:
            diff = length1 - length2
            for _ in range(diff):
                n1 = n1.next

    while n1 != None and n2 != None:
        if n1 == n2:
            return n1
        n1 = n1.next
        n2 = n2.next

    return None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

f = Node(2)

a.next = b
b.next = c
c.next = d
d.next = e

f.next = c

intersection = intersection(a, f)
print(intersection.value)
