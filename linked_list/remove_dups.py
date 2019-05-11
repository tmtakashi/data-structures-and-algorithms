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


def remove_dups(head):
    seen = set()
    prev = None
    current = head
    while current.next != None:
        if current.value in seen:
            prev.next = current.next
        else:
            seen.add(current.value)
            prev = current
        current = current.next


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(1)
    d = Node(5)

    a.next = b
    b.next = c
    c.next = d

    remove_dups(a)

    while a != None:
        print(a.value)
        a = a.next
