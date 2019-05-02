class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def cycle_check(node):
    first_node = node
    while node.next != None:
        node = node.next
        if node == first_node:
            return True
    return False


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.next = b
    b.next = c

    print(cycle_check(a))

    c.next = a

    print(cycle_check(a))
