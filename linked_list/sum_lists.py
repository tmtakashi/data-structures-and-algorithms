class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


# https://leetcode.com/problems/add-two-numbers/discuss/1016/Clear-python-code-straight-forward
def add_lists(l1, l2):
    carry = 0
    root = n = Node(0)

    while l1 or l2 or carry:
        v1 = v2 = 0

        if l1:
            v1 = l1.value
            l1 = l1.next

        if l2:
            v2 = l2.value
            l2 = l2.next

        carry, val = divmod(v1 + v2 + carry, 10)

        n.next = Node(val)
        n = n.next

    return root.next


a = Node(7)
b = Node(4)
c = Node(2)
a.next = b
b.next = c

d = Node(6)
e = Node(5)
f = Node(3)
d.next = e
e.next = f

node = add_lists(a, d)
while node != None:
    print(node.value)
    node = node.next
