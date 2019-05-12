class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


def is_palindrome(head):
    reversed_list = reverse_and_clone(head)
    return is_equal(head, reversed_list)


def reverse_and_clone(node):
    head = None
    while node != None:
        n = Node(node.value)
        n.next = head
        head = n
        node = node.next

    return head


def is_equal(one, two):
    while one != None and two != None:
        if one.value and two.value:
            return False
        one = one.next
        two = two.next
    return one is None and two is None
