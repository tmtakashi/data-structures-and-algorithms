def is_palindrome(head):
    fast = head
    slow = head
    stack = []

    while fast != None and fast.next != None:
        stack.append(slow.value)
        fast = fast.next.next
        slow = slow.next

    if fast != None:
        slow = slow.next

    while slow != None:
        top = stack.pop()

        if top != slow.value:
            return False
        slow = slow.next

    return True
