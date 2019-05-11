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


def delete_node(head, value):
    n = head

    if n.value == value:
        return head.next

    while n.next != None:
        if n.next.value == value:
            n.next = n.next.next
            return head
        n = n.next

    return head
