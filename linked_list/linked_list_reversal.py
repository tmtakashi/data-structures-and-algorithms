class Node(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:
        current = current.next
        current.next = previous

        previous = current
        current = nextnode

    return previous
