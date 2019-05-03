class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextnode = None


# def nth_to_last_node(n, head):
#     current = head
#     num2node = {}
#     i = 1
#     while current:
#         num2node[i] = current
#         current = current.nextnode
#         i += 1
#     list_len = len(num2node)

#     return num2node[list_len - n + 1]


# BETTER SOLUTION (less space complexity)
def nth_to_last_node(n, head):
    right_pointer = head
    left_pointer = head

    # move the right pointer (n-1) steps ahead
    for _ in range(n - 1):
        if not right_pointer.nextnode:
            raise LookupError('n is greater than the node length.')
        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)

    a.nextnode = b
    b.nextnode = c
    c.nextnode = d
    d.nextnode = e

    print(nth_to_last_node(2, a).value)
